#!/usr/bin/python3

import brownie.network as network
import time
from brownie import accounts
from brownie.project import load as load_project

# Admin account
deployer = accounts.load("admin")
REQUIRED_CONFIRMATIONS = 1
# publish or not the source code to Etherscan
publish = False

daoContracts = load_project("curvefi/curve-dao-contracts@1.2.0")
ERC20CRV = daoContracts.ERC20CRV
VotingEscrow = daoContracts.VotingEscrow
GaugeController = daoContracts.GaugeController
Minter = daoContracts.Minter


def _tx_params():
    return {
        "from": deployer,
        "required_confs": REQUIRED_CONFIRMATIONS
    }

def main():
    # Rinkeby at 0x9e5fb7314e5AAB6221489dDFCf3dC34505941A9C
    lp_token = ERC20CRV.deploy("Curve DAO Token", "CRV", 18, _tx_params(), publish_source=publish)
    
    # Rinkeby at 0x79D40735c9Ae990D69b89f1eb45dd6B3330c6fe2
    votingEscrow = VotingEscrow.deploy(lp_token, "Vote-escrowed CRV", "veCRV", "1.0.0", _tx_params(), publish_source=publish)  
    
    # Rinkeby at 0x7C530aE9FE6f877D4df51a1eCef03ea217F7879e
    controller = GaugeController.deploy(lp_token, votingEscrow, _tx_params(), publish_source=publish)  
    
    # Rinkeby at 0x4549D553C1675B3027F8b528Aa954AFeEB3b2d64
    minter = Minter.deploy(lp_token, controller, _tx_params(), publish_source=publish)
    lp_token.set_minter(minter, _tx_params())

    time.sleep(1)
    
    