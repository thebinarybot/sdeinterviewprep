class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s) == sorted(t):
            return True
        return False

# Question: https://leetcode.com/problems/valid-anagram/submissions/1501207111/