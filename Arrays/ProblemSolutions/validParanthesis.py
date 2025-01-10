class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {')':'(', ']':'[', '}':'{'}

        for char in s:
            if char in bracket_map.values():
                stack.append(char)
            elif char in bracket_map.keys():
                if len(stack) == 0 or bracket_map[char] != stack.pop():
                    return False
        
        return len(stack) == 0

# Question: https://leetcode.com/problems/valid-parentheses/