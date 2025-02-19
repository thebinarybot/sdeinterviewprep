class Solution:
    def countSubstrings(self, s: str) -> int:
        length = len(s)
        if length == 0:
            return 0
        
        isPalindrome = [[False] * length for _ in range(length)]
        total = length

        # Base Case - All single characters are palindromes themselves
        for i in range(length):
            isPalindrome[i][i] = True
        
        # Base Case - Check 2 character substrings are palindromes or not
        for i in range(length-1):
            j = i+1
            if s[i] == s[j]:
                isPalindrome[i][j] = True
                total += 1
        
        # Check if substrings of length >=3 are palindromes
        for sub_length in range(3, length+1):
            for start in range(0, length - sub_length + 1):
                end = start + sub_length - 1 

                if s[start] == s[end] and isPalindrome[start+1][end-1]:
                    isPalindrome[start][end] = True
                    total += 1
        
        return total

# Question: https://leetcode.com/problems/palindromic-substrings/submissions/1546766527/