# DEX Stablecoin strategies

This project has several objectives:

- Create a mintable stablecoin using the ERC20 standard.
- Create a metapool with this stablecoin and the 3pool (DAI, USDC, USDT) on Curve
- Create a strategy to improve the slippage incured when swapping stablecoins on the metapool. We explore rerouting to Uniswap v2 and in later versions we will explore rerouting to 1inch and strategies leveraging flashloans of Aave.

This project cointains all the smart contracts deployed, and some scripts used for deployment. Most files were forked from Curve.fi repository. We deploy most of the files on the Rinkeby test network of Ethereum.

## Testing and Development

### Dependencies

- [python3](https://www.python.org/downloads/release/python-368/) from version 3.6 to 3.8, python3-dev
- [brownie](https://github.com/iamdefinitelyahuman/brownie) - tested with version [1.13.2](https://github.com/eth-brownie/brownie/releases/tag/v1.13.2)
- [ganache-cli](https://github.com/trufflesuite/ganache-cli) - tested with version [6.12.1](https://github.com/trufflesuite/ganache-cli/releases/tag/v6.12.1)
- [brownie-token-tester](https://github.com/iamdefinitelyahuman/brownie-token-tester) - tested with version [0.1.0](https://github.com/iamdefinitelyahuman/brownie-token-tester/releases/tag/v0.1.0)

Curve contracts are compiled using [Vyper](https://github.com/vyperlang/vyper), however installation of the required Vyper versions is handled by Brownie.

Uniswap and other contracts are compiled using Solidity. Installation is also managed by Brownie.

### Setup

To get started, first create and initialize a Python [virtual environment](https://docs.python.org/3/library/venv.html).

```bash
python3 -m venv ./venv
source venv/bin/activate
```

Next, install the developer dependencies:

```bash
pip install -r requirements.txt
```

## Deployment on Rinkeby

To run the scripts, you need

1. Set the accounts to deploy, in this we use mainly the "admin account"
   ```bash
   brownie accounts new admin
   ```
   Paste your private key and set the account password.
2. Set your Infura ID as an enviroment variable called WEB3_INFURA_PROJECT_ID or by running
   ```bash
   export WEB3_INFURA_PROJECT_ID=YOUR_KEY_HERE
   ```
3. Follow the deployment instructions under `DEPLOYMENT.md`.
4. To deploy a file in the scripts folder, just write

   ```bash
   brownie run DEPLOY_FILE --network rinkeby
   ```
