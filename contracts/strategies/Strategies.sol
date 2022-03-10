// SPDX-License-Identifier: GPL-3.0
pragma solidity 0.8.11;

// We create the interfaces to the contracts we will be calling
interface IStableCoin {
    function approve(
        address spender, 
        uint256 amount
        ) external returns (bool);
    
    function transferFrom(
        address sender, 
        address recipient, 
        uint256 amount
        ) external returns (bool);
    
    function balanceOf(
        address account
        ) external view returns (uint256);
    
    function transfer(
        address recipient, 
        uint256 amount
        ) external returns (bool);
}

interface IStableSwapMyUSD {
    function get_dy_underlying(
        int128 i, 
        int128 j, 
        uint256 dx
        ) external view returns(uint256); 
    
    function exchange_underlying(
        int128 i, 
        int128 j, 
        uint256 dx, 
        uint256 min_dy
        ) external returns(uint256);
}

interface IUniswapV2Router {
    function swapExactTokensForTokens(
        uint256 amountIn, 
        uint256 amountOutMin, 
        address[] calldata path, 
        address to,
        uint256 deadline
        ) external returns(uint[] memory amounts);
}


contract Strategies{
    /**
     * @dev this contract performs an exchange myUSD/USDC following one of two available strategies
     * stableSwapAddress: address of the Stable Swap Metapool
     * strategyAddress: address of the Strategy Swap pool
     * uniRouterAddress: address to UniswapV2 Router contract
     * strategy: True to use the Strategy, False to use UniswapV2
     */
    address public owner;
    address myUSDAddress;
    address usdcAddress;
    address stableSwapAddress;
    address uniRouterAddress;
    bool public strategy;

    event highSlippage(string failure);

    constructor() {
        owner = msg.sender;
        myUSDAddress = 0xf6363612297cD8b51Bf4cC7D88349F5a0170086c;
        usdcAddress = 0x6EA4D174e3f5Ed61bcBFF29CeC8f6959D09016c9;
        stableSwapAddress = 0x0000000000000000000000000000000000000000;
        uniRouterAddress = 0x0000000000000000000000000000000000000000;
        strategy = true;
    }

    function _intDiv(uint256 a, uint256 b) internal pure returns (uint256){
        //returns the integer part of a/b 
        return a/b; 
    }

    modifier onlyOwner {
        require(msg.sender == owner, "Not owner");
        _;
    }

    function setStrategy(bool _strategy) external onlyOwner{
        /** Switch between our strategy and UniswapV2 strategy
         * @param _strategy true for strategy, false for Uniswap
         */ 
        require(_strategy != strategy, "Strategy already selected");
        strategy = _strategy;
    }

    function _swapStrategy(uint256 _dx, uint256 _min_dy) internal returns(uint256) {
        /** We split the swap between StableSwap and UniswapV2
         * @param _dx amount of myUSD to echange
         * @param _min_dy minimum amount of USDC to receive
         */ 
        uint256 dy1 = IStableSwapMyUSD(stableSwapAddress).exchange_underlying(0, 2, _intDiv(_dx, 2),_intDiv(_min_dy,10)); //to make it work
        uint256 dy2 = _uniswap(_dx - _intDiv(_dx, 2), _intDiv(_min_dy, 2));
        return dy1 + dy2;
    }

    function _uniswap(uint256 _dx, uint256 _min_dy)  internal returns(uint256){
        /** UniswapV2 exchange
         * @param _dx amount of myUSD to echange
         * @param _min_dy minimum amount of USDC to receive
         */ 
        uint256 deadline = block.timestamp + 600;
        address[] memory path = new address[](2);
        path[0] = myUSDAddress;
        path[1] = usdcAddress;
        uint256 usdcAmount = IUniswapV2Router(uniRouterAddress).swapExactTokensForTokens(_dx, _min_dy, path, address(this), deadline)[1];
        return usdcAmount;
        
    }

    function exchange(uint256 _dx, uint256 _max_slippage) external {
        /**
         * @dev it performs an exchange of myUSD for USDC using the predefined strategy
         * @param _dx amount of myUSD to exchange
         * @param _max_slippage maximal slippage allowed in units/100000 (0.5% <--> 500)
         */
         
        //assert (_max_slippage < 100000);

        // estimate the dy to obtain in the swap and setting the minimal amount after slippage
        //uint256 dy_estimated = IStableSwapMyUSD(stableSwapAddress).get_dy_underlying(0, 2, _dx);
        uint256 min_dy = _intDiv(_dx * (100000 -_max_slippage), 100000); // amount will be rounded

        // transfer the myUSD amount to this contract before transfering it to the swap
        IStableCoin(myUSDAddress).transferFrom(msg.sender, address(this), _dx);

        IStableCoin(myUSDAddress).approve(stableSwapAddress, _dx);

        // @dev Make a big transaction now in order to generate big slippage.
        uint256 dy;
        // try to swap with the determined amount
        try IStableSwapMyUSD(stableSwapAddress).exchange_underlying(0, 2, _dx, min_dy) returns (uint256 _dy) {
            dy = _dy;
        }
        catch Error(string memory _err) {
            emit highSlippage(_err);

            IStableCoin(myUSDAddress).approve(stableSwapAddress, 0); // Avoid double ERC20 approve attack

            if (strategy) {
                // Reroute to my strategy 
                IStableCoin(myUSDAddress).approve(stableSwapAddress, _intDiv(_dx, 2));
                IStableCoin(myUSDAddress).approve(uniRouterAddress, _dx - _intDiv(_dx, 2));
                
                dy = _swapStrategy(_dx, _intDiv(min_dy,1));
            }
            else {
                // Reroute to UniswapV2
                IStableCoin(myUSDAddress).approve(uniRouterAddress, _dx);

                dy = _uniswap(_dx, _intDiv(min_dy,1));
            }
        } 

        // send back all the USDC obtained to msg.sender
        IStableCoin(usdcAddress).transfer(msg.sender, dy);
    }
    
}
