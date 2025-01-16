class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        words.reverse()
        return ' '.join(words)

# Question: https://leetcode.com/problems/reverse-words-in-a-string/submissions/1510754498/