# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        res = n
        left, right = 1, n
        while left <= right:
            mid = left + (right-left) // 2
            if isBadVersion(mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return res

# Question: https://leetcode.com/problems/first-bad-version/