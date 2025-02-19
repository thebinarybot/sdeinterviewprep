class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        result = self.coinChangeMemo(coins, amount, memo)
        return result if result != float('inf') else -1
    
    def coinChangeMemo(self, coins: List[int], amount: int, memo: dict) -> int:
        
        # Base Cases
        if amount in memo:
            return memo[amount]
        if amount == 0:
            return 0
        if amount < 0:
            return float('inf')  
        
        # Store count of minimum coins
        min_coins = float('inf')

        # Logic
        for coin in coins:
            remainder = amount - coin
            res = self.coinChangeMemo(coins, remainder, memo)
            if res != float('inf'):
                min_coins = min(min_coins, res + 1)
        
        memo[amount] = min_coins
        return memo[amount]

# Question: https://leetcode.com/problems/coin-change/