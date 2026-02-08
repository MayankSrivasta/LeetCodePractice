from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]

        for i in range(numRows - 1):
            temp = [0] + res[-1] + [0]
            row = []
            for j in range(len(res[-1]) + 1):
                row.append(temp[j] + temp[j + 1])
            res.append(row)
        return res
    
sol = Solution()
print(sol.generate(5))

#====================================================================================================

# chatgpt solution
# below ones looks much better:-
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        for i in range(numRows):
            # create a row filled with 1s
            row = [1] * (i + 1)


# fill middle elements
# the below loop will only run to fill in the values of the middle elements
            for j in range(1, i):
                row[j] = triangle[i-1][j-1] + triangle[i-1][j]

            triangle.append(row)

        return triangle
    
# Mental Pattern (Interview Gold)
# This problem teaches a key interview mindset:
# Design loops so that edge cases naturally disappear.

# Designing the solution based upon the contraint of the given problem. SO I am designing
# solutiohn so that it by defauutl skips the first 2 rows for calculation.

# think after creating the diagram with indexes filled in for each row & each elements 
# in the rows the programs gets cleared