class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        
        target = len(nums) - 1
        canGo = 0

        for i in range(0, len(nums)):
            canGo = max(canGo, nums[i])
            if canGo >= 1:
                if canGo + i >= target:
                    return True
                canGo -= 1
            else:
                return False

# Question: https://leetcode.com/problems/jump-game/