from brownie import DAI, USDC, USDT, StableSwap3Pool, accounts

# loading Admin address
admin = accounts.load("admin")

# setting Smart Contracts for StableCoins and Swap
dai = DAI.at("")
usdc = USDC.at("")
usdt = USDT.at("")

swap = StableSwap3Pool.at("")
slippage = 0.005

# Setting parameters for the transaction 
params = { 'from': admin }

# Setting amounts to transfer
def allowAndTransfer(am_dai, am_usdc, am_usdt):
    dai.approve(swap,am_dai,params)
    usdc.approve(swap,am_usdc,params)
    usdt.approve(swap,am_usdt,params)

    swap.add_liquidity([am_dai,am_usdc,am_usdt],0,params)

def main():
    allowAndTransfer(10**23, 10**11, 10**11)

 