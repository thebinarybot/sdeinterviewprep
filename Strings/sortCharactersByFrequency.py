class Solution:
    def frequencySort(self, s: str) -> str:
        res = ''
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        
        freq_sorted = dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))
        for key,value in freq_sorted.items():
            res += key*value
        
        return res

# Question: https://leetcode.com/problems/sort-characters-by-frequency/