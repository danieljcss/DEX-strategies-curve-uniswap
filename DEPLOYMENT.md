# Steps to deploy on Rinkeby

1. Deploy all the Stablecoins
   ```bash
   brownie run deployStableCoins.py --network rinkeby
   ```
   Copy the address of the 3 stablecoins DAI, USDC and USDT on `3pool/pooldata.json` and the address of myUSD in `myusd/pooldata.json`. This will mint 1.000.000 of each coin to the account "admin". Copy USDT address to the file `contracts/pools/myusd/StableSwapMyUSD.vy` in line `FEE_ASSET: constant(address)`.
2. Deploy Curve DAO Token (CRV)

   ```bash
   brownie run deployCRV.py --network rinkeby
   ```

   and copy the address of the Minter contract

3. Paste the address of the Minter Contract in both pools variable `MINTER`. The pools files are `deploy3pool.py` and `deployMyUSDpool.py`.

4. Deploy the tripool 3Crv token

   ```bash
   brownie run deploy3pool.py --network rinkeby
   ```

   and copy its address into `myusd/pooldata.json`. Update the StableSwap Adress in `3pool/pooldata.json`

5. Fill adresses in `scripts/addLiquidity3pool.py` and add liquidity to the 3Pool to mine some 3Crv tokens.

   ```bash
      brownie run addLiquidity3pool.py --network rinkeby
   ```

6. Deploy the MyUSD metapool [myUSD,[3Crv]] contract

   ```bash
   brownie run deployMyUSDpool.py --network rinkeby

   ```

7. Add Liquidity to the MetaPool

   ```bash
   brownie run addLiquidityMyUSDpool.py --network rinkeby
   ```

8. Before performing ecxhanges, do not forget to approve the given swap contract the amount you want to convert. You can do that by using the command below (we swap myUSD)
   ```bash
   brownie console --netowrk rinkeby
   >> myUSD.at("ADDRESS_MYUSD").approve("SWAP_CONTRACT_ADDRESS", AMOUNT, {'from': account.load("admin")})
   ```
