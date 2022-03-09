// SPDX-License-Identifier: GPL-3.0

pragma solidity ^0.8.11;

import "@openzeppelin/contracts/token/ERC20/presets/ERC20PresetMinterPauser.sol";

/**
 * @dev myUSD inherits from ERC20PresetMinterPauser the ability to mint and burn
 * tokens. The admin by default is the deployer address.
 *
 * See {ERC20PresetMinterPauser-constructor} for more details.
 */
contract myUSD is ERC20PresetMinterPauser("Stable myUSD", "myUSD") {
    /**
     * @dev The constructor determines the initial supply of myUSD and assign them
     * to the deployer address
     *
     * @param initialSupply initial supply of myUSD. See function decimals below.
     */
    constructor(uint256 initialSupply){
        _mint(msg.sender, initialSupply);
    }
    
    /**
     * @dev This function overrides the defualt number of decimals of the myUSD token.
     * We set it to 6 following the convention for USD stablecoins like USDC, USDT
     */
    function decimals() public view virtual override returns (uint8) {
        return 6;
    }
}