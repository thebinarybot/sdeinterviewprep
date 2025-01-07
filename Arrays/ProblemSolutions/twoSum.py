class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(0, len(nums)):
            if target - nums[i] not in hashmap:
                hashmap[nums[i]] = i
            else:
                return [hashmap[target-nums[i]], i]

# Question: https://leetcode.com/problems/two-sum/