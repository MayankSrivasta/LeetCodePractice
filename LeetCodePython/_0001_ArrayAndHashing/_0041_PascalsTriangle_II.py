from typing import List
class Solution:
    # APPROACH - 1
    # visual representation for understanding the solution
    # is given in the neetcode video go through it.
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]
        for i in range(rowIndex):
            next_row = [0] * (len(res) + 1)
            for j in range(len(res)): 
                next_row[j] += res[j]
                next_row[j+1] += res[j]
            res = next_row
        return res

# APPROACH - 2
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for i in range(rowIndex):
            temp = [0] + row + [0]
            row = []
            for j in range(len(temp) - 1):
                row.append(temp[j] + temp[j + 1])
        return row

sol = Solution()
print(sol.getRow(3))