import json

import brownie.network as network
#from brownie.network.gas.strategies import GasNowScalingStrategy
from brownie import accounts
from brownie.project import load as load_project
from brownie.project.main import get_loaded_projects

# set a throwaway admin account here
DEPLOYER = accounts.load("admin") # Rinkeby account
REQUIRED_CONFIRMATIONS = 1

# deployment settings
# most settings are taken from `contracts/pools/{POOL_NAME}/pooldata.json`
POOL_NAME = "myusd"

# temporary owner address Metamask Admin Rinkeby
POOL_OWNER = accounts.load("admin")
GAUGE_OWNER = accounts.load("admin")

# Curve DAO token Minter address
MINTER = ""

def _tx_params():
    return {
        "from": DEPLOYER,
        "required_confs": REQUIRED_CONFIRMATIONS
    }


def main():
    project = get_loaded_projects()[0]
    balance = DEPLOYER.balance()

    # we load data about the deployment from `pooldata.json`
    contracts_path = project._path.joinpath("contracts/pools")
    with contracts_path.joinpath(f"{POOL_NAME}/pooldata.json").open() as fp:
        pool_data = json.load(fp)
    
    # we get the name of the Swapping contract without the suffix
    swap_name = next(i.stem for i in contracts_path.glob(f"{POOL_NAME}/StableSwap*"))

    # we prepare the variables to deploy the swapping and the token contract 
    swap_deployer = getattr(project, swap_name)
    token_deployer = getattr(project, pool_data.get("lp_contract"))
    
    # we load the address of the underlying coins and its wrapped versions in the pool
    underlying_coins = [i["underlying_address"] for i in pool_data["coins"]]
    wrapped_coins = [i.get("wrapped_address", i["underlying_address"]) for i in pool_data["coins"]]

    # we set the base pool to interact with in the metapool
    base_pool = None
    if "base_pool" in pool_data:
        with contracts_path.joinpath(f"{pool_data['base_pool']}/pooldata.json").open() as fp:
            base_pool_data = json.load(fp)
            base_pool = base_pool_data["swap_address"]

    # deploy the Curve token with the arguments in the data
    token_args = pool_data["lp_constructor"]
    token = token_deployer.deploy(token_args["name"], token_args["symbol"], 18, 0, _tx_params())


    # deploy the swapping pool
    abi = next(i["inputs"] for i in swap_deployer.abi if i["type"] == "constructor")
    args = pool_data["swap_constructor"]
    args.update(
        _coins=wrapped_coins,
        _underlying_coins=underlying_coins,
        _pool_token=token,
        _base_pool=base_pool,
        _owner=POOL_OWNER,
    )
    deployment_args = [args[i["name"]] for i in abi] + [_tx_params()]

    swap = swap_deployer.deploy(*deployment_args)

    # set the minter for myusd metapool
    token.set_minter(swap, _tx_params())
   

    # deploy the liquidity gauge
    LiquidityGaugeV3 = load_project("curvefi/curve-dao-contracts@1.2.0").LiquidityGaugeV3
    LiquidityGaugeV3.deploy(token, MINTER, GAUGE_OWNER, _tx_params())

    
    # deploy the deposit zap
    zap_name = next((i.stem for i in contracts_path.glob(f"{POOL_NAME}/Deposit*")), None)
    if zap_name is not None:
        zap_deployer = getattr(project, zap_name)

        abi = next(i["inputs"] for i in zap_deployer.abi if i["type"] == "constructor")
        args = {
            "_coins": wrapped_coins,
            "_underlying_coins": underlying_coins,
            "_token": token,
            "_pool": swap,
            "_curve": swap,
        }
        deployment_args = [args[i["name"]] for i in abi] + [_tx_params()]

        zap_deployer.deploy(*deployment_args)


    print(f"Gas used in deployment: {(balance - DEPLOYER.balance()) / 1e18:.4f} ETH")



# To deploy on Rinkeby we run: brownie run deployMyUSD.py --network rinkeby