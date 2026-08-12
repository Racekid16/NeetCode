class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:          
        memo = {}
        
        # the fewest number of coins needed to make up i amount of money
        def helper(i):
            if i == 0:
                return 0
            
            if i in memo:
                return memo[i]
            
            res = float('inf')

            for coin in coins:
                if i - coin >= 0:
                    res = min(res, helper(i - coin) + 1)
            
            memo[i] = res
            return memo[i]

        minCoins = helper(amount)
        if minCoins == float('inf'):
            return -1
        return minCoins