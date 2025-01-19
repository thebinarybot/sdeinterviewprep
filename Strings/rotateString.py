class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        return goal in s+s

# Question: https://leetcode.com/problems/rotate-string/