from brownie import DAI, USDC, USDT, StableSwap3Pool, accounts

# loading Admin address
admin = accounts.load("admin")

# setting Smart Contracts for StableCoins and Swap
dai = DAI.at("0x692826529ed5b2114A374AB83ac1a252b5F5A823")
usdc = USDC.at("0x6EA4D174e3f5Ed61bcBFF29CeC8f6959D09016c9")
usdt = USDT.at("0x59dc618fA07328D9046C93854B6805A3513F3Ee0")

swap = StableSwap3Pool.at("0xF996af86dFcc4D6C8fC8b5Aab20767C891B714A7")
#slippage = 0.005

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

 