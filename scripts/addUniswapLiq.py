from brownie import myUSD, USDC, UniswapV2Router02, accounts

#UniswapV2Pair, UniswapV2Factory,

# loading Admin address
admin = accounts.load("admin")
params = { 'from': admin }

# setting Smart Contracts for Stablecoins
myusd = myUSD.at("")
usdc = USDC.at("")

# setting Smart Contracts for Uniswap
uniRouter = UniswapV2Router02.at("")

#uniFactory = UniswapV2Factory.at("")
#uniFactory.createpair(myusd, usdc)

# pair created with factory
#uniPair = UniswapV2Pair.at("")


# Setting amounts to transfer
def allowAndTransfer(am_myusd, am_usdc):
    myusd.approve(uniRouter,am_myusd, params)
    usdc.approve(uniRouter, am_usdc, params)

    #uniRouter.addLiquidity(myusd, usdc, am_myusd, am_usdc, 0, 0, uniPair, params)

def main():
    allowAndTransfer(5*10**11, 5*10**11)