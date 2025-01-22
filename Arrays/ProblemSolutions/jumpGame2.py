class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        n = len(nums)
        farthest = 0
        current = 0
        jumps = 0

        for i in range(n-1):
            farthest = max(farthest, i+nums[i])
            if i == current:
                jumps += 1
                current = farthest
                if current >= n-1:
                    break
        return jumps

# Question: https://leetcode.com/problems/jump-game-ii/