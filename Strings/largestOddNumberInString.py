class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num)-1,-1,-1):
            if int(num[i]) % 2 != 0:
                return ''.join(num[0:i+1])
        return ''

# Question: https://leetcode.com/problems/largest-odd-number-in-string/