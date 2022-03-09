#!/usr/bin/python3

import brownie.network as network
from brownie import myUSD, DAI, USDC, USDT, accounts

deployer = accounts.load("admin")
# publish or not the source code to Etherscan
publish = False


def main():
    """@dev it deploys the 4 stablecoins we will be using"""

    myUSD.deploy(1e12, {"from": deployer}, publish_source=publish)
    DAI.deploy(1e24, {"from": deployer}, publish_source=publish)
    USDC.deploy(1e12, {"from": deployer}, publish_source=publish)
    USDT.deploy(1e12, {"from": deployer}, publish_source=publish)