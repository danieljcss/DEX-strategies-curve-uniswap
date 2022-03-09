from brownie import myUSD, StableSwapMyUSD, accounts

# loading Admin address
admin = accounts.load("admin")

# setting Smart Contracts for StableCoins and Swap
myusd = myUSD.at("")

swap = StableSwapMyUSD.at("")

# Setting parameters for the transaction 
params = { 'from': admin }

# Setting amounts to transfer
def allowAndSwap(am_myusd,token_index):
    """
    @notice Perform an exchange between myUSD and one other stablecoin of the 3pool
    @dev Index values can be found via the `underlying_coins` public getter method
    @param am_myusd Amount of myUSD being exchanged
    @param token_index Index value of the underlying stablecoin to recieve
    @return Actual amount of `token_index` received
    """
    myusd.approve(swap,am_myusd,params)

    input("Press Enter to continue...")
    swap.exchange_underlying(0,token_index,am_myusd,0,params)

def main():
    #Swap myUSD for USDC
    allowAndSwap(10000000000,2)
