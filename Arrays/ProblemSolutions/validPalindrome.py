import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = s.lower()
        string = re.sub(r'[^a-zA-Z0-9]','',string) 
        start = 0
        end = len(string)-1
        while(start < end):
            if string[start] != string[end]:
                return False
            start+=1
            end-=1
        return True

# Question: https://leetcode.com/problems/valid-palindrome/