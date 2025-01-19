class Solution:
    def maxDepth(self, s: str) -> int:
        maxcount = 0
        count = 0
        for char in s:
            if char == "(":
                count += 1
                maxcount = max(count, maxcount)
            elif char == ")":
                count -= 1
        return maxcount
    
# Question: https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/