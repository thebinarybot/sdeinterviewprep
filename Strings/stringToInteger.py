class Solution:
    def myAtoi(self, s: str) -> int:
        
        # Remove whitespace
        s = s.strip()
        if not s:
            return 0

        # Determine Sign
        sign = 1
        if s[0] == "-":
            sign = -1
            s = s[1:]
        elif s[0] == "+":
            s = s[1:]
        
        # Convert
        result = 0
        for char in s:
            if not char.isdigit():
                break
            result = result * 10 + int(char)

        # Check result in range
        result = sign * result
        if result < -2**31:
            return -2**31
        elif result > 2**31 - 1:
            return 2**31 - 1
        else:
            return result

# Question: https://leetcode.com/problems/string-to-integer-atoi/