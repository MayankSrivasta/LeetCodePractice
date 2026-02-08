from typing import List
class NumMatrix:
# 2d prefix sum NeetCode.io

    def __init__(self, matrix: list[list[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.sumMat = [[0] * (COLS + 1) for _ in range(ROWS + 1)]

#       above line can be written as
        # self.prefix = []  # Initialize an empty list
        # for _ in range(rows + 1):            # Loop over each row
        #     row = [0] * (cols + 1)           # Create a row with (cols + 1) zeros
        #     self.prefix.append(row)         # Append the row to the prefix matrix

# so there are 2 approaches for doing the pre-processing, one by Neetcode.io given below, other
# by just using the formula in sumRegion.       

        for r in range(ROWS):
            prefix = 0
            for c in range(COLS):
                prefix += matrix[r][c]
                above = self.sumMat[r][c + 1]
                self.sumMat[r + 1][c + 1] = prefix + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        bottomRight = self.sumMat[row2][col2]
        above = self.sumMat[row1 - 1][col2]
        left = self.sumMat[row2][col1 - 1]
        topLeft = self.sumMat[row1 - 1][col1 - 1]
        return bottomRight - above - left + topLeft
    
#====================================================================================================

#  chatgpt approach.
# 2nd approach for doing Pre-Processing based on the formula itself
    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.prefix = [[0] * (cols + 1) for _ in range(rows + 1)]

        for r in range(rows):
            for c in range(cols):
                self.prefix[r+1][c+1] = matrix[r][c] + self.prefix[r][c+1] + self.prefix[r+1][c] - self.prefix[r][c]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.prefix[row2+1][col2+1]     #  + bottom-right area up to (row2, col2)
            - self.prefix[row1][col2+1]     #  - area above the submatrix
            - self.prefix[row2+1][col1]     #  - area to the left of the submatrix
            + self.prefix[row1][col1]       #  + add back the overlapping top-left corner (which was subtracted twice)
        )
