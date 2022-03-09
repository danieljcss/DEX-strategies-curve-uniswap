# /contracts/pools/myusd

myUSD metapool, allowing swaps via the Curve [tri-pool](../3pool).

## Contracts

- [`DepositMyUSD`](DepositMyUSD.vy): Depositor contract, used to wrap underlying tokens prior to depositing them into the pool
- [`StableSwapMyUSD`](StableSwapMyUSD.vy): My stablecoin AMM contract

## Deployments

- [`CurveContractV2`](../../tokens/CurveTokenV2.vy): [](https://rinkeby.etherscan.io/address/)
- [`DepositMyUSD`](DepositMyUSD.vy): [](https://rinkeby.etherscan.io/address/)
- [`LiquidityGaugeV3`](../../gauges/LiquidityGaugeV3.vy): [](https://rinkeby.etherscan.io/address/)
- [`StableSwapMyUSD`](StableSwapMyUSD.vy): [](https://rinkeby.etherscan.io/address/)

## Stablecoins

myUSD metapool utilizes the supports swaps between the following assets:

## Direct swaps

Direct swaps are possible between myUSD and the Curve tri-pool LP token.

- `myUSD`: [](https://rinkeby.etherscan.io/address/)
- `3CRV`: [](https://rinkeby.etherscan.io/address/)

## Base Pool coins

The tri-pool LP token may be wrapped or unwrapped to provide swaps between myUSD and the following stablecoins:

- `DAI`: [](https://rinkeby.etherscan.io/address/)
- `USDC`: [](https://rinkeby.etherscan.io/address/)
- `USDT`: [](https://rinkeby.etherscan.io/address/)
