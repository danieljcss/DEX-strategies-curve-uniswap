// SPDX-License-Identifier: GPL-3.0

pragma solidity ^0.8.11;

import "@openzeppelin/contracts/token/ERC20/presets/ERC20PresetMinterPauser.sol";

/**
 * @dev inherits from ERC20PresetMinterPauser the ability to mint and burn
 * tokens. The admin by default is the deployer address.
 *
 * See {ERC20PresetMinterPauser-constructor} for more details.
 */
contract USDT is ERC20PresetMinterPauser("Theter USD", "USDT") {
    /**
     * @dev The constructor determines the initial supply of USDT and assign them
     * to the deployer address
     *
     * @param initialSupply initial supply of USDT. See function decimals below.
     */
    constructor(uint256 initialSupply){
        _mint(msg.sender, initialSupply);
    }
    
    /**
     * @dev This function overrides the defualt number of decimals of the USDT token.
     */
    function decimals() public view virtual override returns (uint8) {
        return 6;
    }
}