class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def climb(i):
            if i in memo:
                return memo[i]
            if i <=2:
                return i
            memo[i] = climb(i-1) + climb(i-2)
            return memo[i]
        
        return climb(n)

# Question: https://leetcode.com/problems/climbing-stairs/