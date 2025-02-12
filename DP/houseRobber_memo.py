class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)-1
        memo = {}
        def robHelper(i):
            if i in memo:
                return memo[i]
            # base case
            if i < 0:
                return 0
            memo[i] = max(nums[i] + robHelper(i-2), robHelper(i-1))
            return memo[i]
        return robHelper(n)

# Question: https://leetcode.com/problems/house-robber/