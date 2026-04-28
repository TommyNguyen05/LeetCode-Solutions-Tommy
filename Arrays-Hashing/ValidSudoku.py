# Leetcode problem 36: Valid Sudoku
# Difficulty: Medium
# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

import collections
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Create a dictionary where every new key automatically starts with an empty set.
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set) # key = (r/3, c/3)
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".": # empty cell
                    continue
                # Check if have found duplicate, if yes, the board is invalid immediately
                if (board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r//3, c//3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
        return True
    
# Test cases:
# Case 1: board = 
# [["5","3",".",".","7",".",".",".","."],
#  ["6",".",".","1","9","5",".",".","."],
#  [".","9","8",".",".",".",".","6","."],
#  ["8",".",".",".","6",".",".",".","3"],
#  ["4",".",".","8",".","3",".",".","1"],
#  ["7",".",".",".","2",".",".",".","6"],
#  [".","6",".",".",".",".","2","8","."],
#  [".",".",".","4","1","9",".",".","5"],
#  [".",".",".",".","8",".",".","7","9"]]
# Case 2: board =
# [["8","3",".",".","7",".",".",".","."],
#  ["6",".",".","1","9","5",".",".","."],
#  [".","9","8",".",".",".",".","6","."],
#  ["8",".",".",".","6",".",".",".","3"],
#  ["4",".",".","8",".","3",".",".","1"],
#  ["7",".",".",".","2",".",".",".","6"],
#  [".","6",".",".",".",".","2","8","."],
#  [".",".",".","4","1","9",".",".","5"],
#  [".",".",".",".","8",".",".","7","9"]]

if __name__ == "__main__":
    sol = Solution()
    
    board1 = [["5","3",".",".","7",".",".",".","."],
              ["6",".",".","1","9","5",".",".","."],
              [".","9","8",".",".",".",".","6","."],
              ["8",".",".",".","6",".",".",".","3"],
              ["4",".",".","8",".","3",".",".","1"],
              ["7",".",".",".","2",".",".",".","6"],
              [".","6",".",".",".",".","2","8","."],
              [".",".",".","4","1","9",".",".","5"],
              [".",".",".",".","8",".",".","7","9"]]
    
    board2 = [["8","3",".",".","7",".",".",".","."],
              ["6",".','.','1','9','5','.','.','.'"],
              [".",'9','8','.','.','.','.','6','.'],
              ['8','.','.','.','6','.','.','.','3'],
              ['4','.','.','8','.','3','.','.','1'],
              ['7','.','.','.','2','.','.','.','6'],
              ['.','6','.','.','.','.','2','8','.'],
              ['.','.','.','4','1','9','.','.','5'],
              ['.','.','.','.','8','.','.','7','9']]
    
    print(sol.isValidSudoku(board1)) # should return True
    print(sol.isValidSudoku(board2)) # should return False