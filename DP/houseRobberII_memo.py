class Solution:
    def rob(self, nums: List[int]) -> int:
        n1 = len(nums) - 1 
        if n1 == 0:
            return nums[0]
        
        n2 = len(nums) - 2 
        memo1 = {}
        memo2 = {}

        def robHelper1(i):
            if i in memo1:
                return memo1[i]
            if i <= 0:
                return 0
            memo1[i] = max(nums[i] + robHelper1(i-2), robHelper1(i-1)) 
            return memo1[i]

        def robHelper2(i):
            if i in memo2:
                return memo2[i]
            if i < 0:
                return 0
            memo2[i] = max(nums[i] + robHelper2(i-2), robHelper2(i-1))
            return memo2[i]

        return max(robHelper1(n1), robHelper2(n2))

# Question: https://leetcode.com/problems/house-robber-ii/