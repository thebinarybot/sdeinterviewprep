class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        if length == 0:
            return ""

        isPalindrome = [[False] * length for _ in range(length)]
        best_start, best_length = 0, 1

        # Base Case: Single characters are palindromes 
        for i in range(length):
            isPalindrome[i][i] = True 
        
        # Base Case: Check 2 character substrings by comparing start and end
        for i in range(length-1):
            j = i+1
            if s[i] == s[j]:
                isPalindrome[i][j] = True
                best_start = i
                best_length = 2
        
        # Iterate for substrings of length >= 3 
        for sub_length in range(3, length + 1):
            for start in range(0, length - sub_length + 1):
                end = start + sub_length - 1

                if s[start] == s[end] and isPalindrome[start+1][end-1]:
                    isPalindrome[start][end] = True
                    best_start = start
                    best_length = sub_length
        
        return s[best_start:best_start+best_length]

# Question: https://leetcode.com/problems/longest-palindromic-substring/