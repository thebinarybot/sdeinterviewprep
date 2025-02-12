class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = {}

        def minCost(i):
            
            if i in memo:
                return memo[i]

            # Start: From index 0 or 1
            # End : Last or last-before index
            if i == n-1 or i == n-2:
                return cost[i]
            
            option1 = cost[i] + minCost(i+1)
            option2 = cost[i] + minCost(i+2)
            memo[i] = min(option1, option2)
            return memo[i]
        
        return min(minCost(0), minCost(1))

# Question: https://leetcode.com/problems/min-cost-climbing-stairs/