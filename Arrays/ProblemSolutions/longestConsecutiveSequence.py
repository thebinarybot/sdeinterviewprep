class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        maxlength = 1
        length = 1
        numssorted = sorted(set(nums))
        for i in range(1,len(numssorted)):
            if numssorted[i] - numssorted[i-1] == 1:
                length += 1
                maxlength = max(length,maxlength)
            else:
                length = 1
        return maxlength    

# Question: https://leetcode.com/problems/longest-consecutive-sequence/