class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = nums[0]
        current = 0
        for num in nums:
            if current < 0:
                current = 0
            current += num
            maxsum = max(current, maxsum)
        return maxsum

# Question: https://leetcode.com/problems/maximum-subarray/