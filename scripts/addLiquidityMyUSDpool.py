from brownie import myUSD, CurveTokenV2, StableSwapMyUSD, accounts

# loading SAdmin address
admin = accounts.load("admin")

# setting Smart Contracts for StableCoins and Swap
myusd = myUSD.at("0xf6363612297cD8b51Bf4cC7D88349F5a0170086c")
tripool = CurveTokenV2.at("0xcf86Bdc5D9Bdc2eDf00cBfB694D14CbF00975710")


swap = StableSwapMyUSD.at("0x933D452280Dd9F14464631F2E26523ca083C1a32")
slippage = 0.005

# Setting parameters for the transaction 
params = { 'from': admin }

# Setting amounts to transfer
def allowAndTransfer(am_myusd, am_3crv):
    myusd.approve(swap,am_myusd,params)
    tripool.approve(swap,am_3crv,params)

    swap.add_liquidity([am_myusd,am_3crv],0,params)

def main():
    allowAndTransfer(10**11, 10**23)
