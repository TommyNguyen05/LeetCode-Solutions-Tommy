# Leetcode 74. Search a 2D Matrix
# Difficulty: Medium
# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        left, right = 0, row * col - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            mid_value = matrix[mid // col][mid % col]
            
            if mid_value == target:
                return True
            elif mid_value < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
    
# Test cases:
# Case 1: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Case 2: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Case 3: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 16

if __name__ == "__main__":
    sol = Solution()
    
    matrix1 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target1 = 3
    
    matrix2 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target2 = 13
    
    matrix3 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target3 = 16
    
    print(sol.searchMatrix(matrix1, target1)) # should return True
    print(sol.searchMatrix(matrix2, target2)) # should return False
    print(sol.searchMatrix(matrix3, target3)) # should return True