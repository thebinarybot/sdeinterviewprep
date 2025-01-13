class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        left, right = 0, m * n - 1
    
        while left <= right:
            mid = (left + right) // 2
            row, col = mid // n, mid % n
            mid_val = matrix[row][col]
        
            if mid_val == target:
                return True
            elif mid_val < target:
                left = mid + 1
            else:
                right = mid - 1
    
        return False

# Question: https://leetcode.com/problems/search-a-2d-matrix/