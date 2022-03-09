#!/usr/bin/python3

import brownie.network as network
from brownie import Strategies, accounts

# Account saved with brownie accounts new admin
deployer = accounts.load("admin")
# publish or not the source code to Etherscan
publish = False


def main():
    """@dev it deploys the Strategies contract"""

    Strategies.deploy({"from": deployer}, publish_source=publish)

# 