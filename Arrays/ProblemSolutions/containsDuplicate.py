class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numsmap = {}
        for i in nums:
            if i not in numsmap:
                numsmap[i] = 1
            else:
                return True
        return False

# Question: https://leetcode.com/problems/contains-duplicate/