from brownie import myUSD, CurveTokenV2, StableSwapMyUSD, accounts

# loading SAdmin address
admin = accounts.load("admin")

# setting Smart Contracts for StableCoins and Swap
myusd = myUSD.at("")
tripool = CurveTokenV2.at("")


swap = StableSwapMyUSD.at("")
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
