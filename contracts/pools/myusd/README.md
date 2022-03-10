# /contracts/pools/myusd

myUSD metapool, allowing swaps via the Curve [tri-pool](../3pool).

## Contracts

- [`DepositMyUSD`](DepositMyUSD.vy): Depositor contract, used to wrap underlying tokens prior to depositing them into the pool
- [`StableSwapMyUSD`](StableSwapMyUSD.vy): My stablecoin AMM contract

## Deployments

- [`CurveContractV2`](../../tokens/CurveTokenV2.vy): [](https://rinkeby.etherscan.io/address/)
- [`DepositMyUSD`](DepositMyUSD.vy): [0x00e6A2D3067a07b3a167912E116AeE4e0a4B5385](https://rinkeby.etherscan.io/address/0x00e6A2D3067a07b3a167912E116AeE4e0a4B5385)
- [`LiquidityGaugeV3`](../../gauges/LiquidityGaugeV3.vy): [0x2B90cA50FE3aE80B3EC7565d5Df8b602FC08D4E1](https://rinkeby.etherscan.io/address/0x2B90cA50FE3aE80B3EC7565d5Df8b602FC08D4E1)
- [`StableSwapMyUSD`](StableSwapMyUSD.vy): [0x933D452280Dd9F14464631F2E26523ca083C1a32](https://rinkeby.etherscan.io/address/0x933D452280Dd9F14464631F2E26523ca083C1a32)

## Stablecoins

myUSD metapool utilizes the supports swaps between the following assets:

## Direct swaps

Direct swaps are possible between myUSD and the Curve tri-pool LP token.

- `myUSD`: [0xf6363612297cD8b51Bf4cC7D88349F5a0170086c](https://rinkeby.etherscan.io/address/0xf6363612297cD8b51Bf4cC7D88349F5a0170086c)
- `3CRV`: [0xcf86Bdc5D9Bdc2eDf00cBfB694D14CbF00975710](https://rinkeby.etherscan.io/address/0xcf86Bdc5D9Bdc2eDf00cBfB694D14CbF00975710)

## Base Pool coins

The tri-pool LP token may be wrapped or unwrapped to provide swaps between myUSD and the following stablecoins:

- `DAI`: [0x692826529ed5b2114A374AB83ac1a252b5F5A823](https://rinkeby.etherscan.io/address/0x692826529ed5b2114A374AB83ac1a252b5F5A823)
- `USDC`: [0x6EA4D174e3f5Ed61bcBFF29CeC8f6959D09016c9](https://rinkeby.etherscan.io/address/0x6EA4D174e3f5Ed61bcBFF29CeC8f6959D09016c9)
- `USDT`: [0x59dc618fA07328D9046C93854B6805A3513F3Ee0](https://rinkeby.etherscan.io/address/0x59dc618fA07328D9046C93854B6805A3513F3Ee0)
