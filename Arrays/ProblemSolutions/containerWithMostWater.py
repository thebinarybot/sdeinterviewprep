class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        res = 0

        while left < right:
            minVal = min(height[left], height[right])
            res = max(res, minVal * (right - left))
            if minVal == height[left]:
                left += 1
            else:
                right -=1

        return res 

# Question: https://leetcode.com/problems/container-with-most-water/