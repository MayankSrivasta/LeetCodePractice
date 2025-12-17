from typing import List


"""
BINARY SEARCH APPROACH:- 
when the values already given is in increasing order, in matrix then it could be written in a 1-D array.
then u can get 'm', then on the basis of 'm' u can figure out where it would like in matrix
by m // COL and m % COL.
"""

class Solution:
    # BINARY SEARCH - ONE PASS


    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        l, r = 0, ROWS * COLS - 1
        while l <= r:
            m = l + (r - l) // 2
            row, col = m // COLS, m % COLS
            if target > matrix[row][col]:
                l = m + 1
            elif target < matrix[row][col]:
                r = m - 1
            else:
                return True
        return False
    

# STAIRCASE SEARCH - its mainly used in case when both row & column are in sorted order
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        r, c = 0, n - 1

        while r < m and c >= 0:
            if matrix[r][c] > target:
                c -= 1
            elif matrix[r][c] < target:
                r += 1
            else:
                return True
        return False
    
"""
You use this method when the matrix has the following properties:

Each row is sorted in increasing order (left → right)

Each column is sorted in increasing order (top → bottom)

🔍 The idea is:
Start from the top-right (or bottom-left) of the matrix, and move like you're walking down a staircase — that's why it's called staircase search.    

Start from the top-right (or bottom-left) of the matrix, and move like you're walking down a staircase — that's why it's called staircase search.
"""