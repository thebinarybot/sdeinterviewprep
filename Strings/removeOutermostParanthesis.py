class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = ""
        open_count = 0 

        for char in s:
            if char == '(' and open_count > 0: 
                result += char 

            if char == ')' and open_count > 1: 
                result += char 

            if char == '(':
                open_count += 1  # Increment open_count for '('
            elif char == ')':
                open_count -= 1  # Decrement open_count for ')'

        return result

# Question: https://leetcode.com/problems/remove-outermost-parentheses/