// SPDX-License-Identifier: GPL-3.0

pragma solidity ^0.8.11;

import "@openzeppelin/contracts/token/ERC20/presets/ERC20PresetMinterPauser.sol";

/**
 * @dev DAI inherits from ERC20PresetMinterPauser the ability to mint and burn
 * tokens. The admin by default is the deployer address.
 *
 * See {ERC20PresetMinterPauser-constructor} for more details.
 */
contract DAI is ERC20PresetMinterPauser("DAI Stablecoin", "DAI") {
    /**
     * @dev The constructor determines the initial supply of DAI and assign them
     * to the deployer address
     *
     * @param initialSupply initial supply of DAI. See function decimals below.
     */
    constructor(uint256 initialSupply){
        _mint(msg.sender, initialSupply);
    }
    
    /**
     * @dev The number of decimals is 18 by default, like DAI
     */
    
}