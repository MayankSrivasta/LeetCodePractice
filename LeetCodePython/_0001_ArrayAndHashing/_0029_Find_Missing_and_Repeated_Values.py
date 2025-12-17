from typing import List
from collections import defaultdict
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        count = defaultdict(int)

        for i in range(n):
            for j in range(n):
                count[grid[i][j]] += 1
        
        double, missing = 0, 0
        for i in range(1, n * n + 1):
            if count[i] == 0:
                missing = i
            if count[i] == 2:
                double = i
        return [double, missing]
    
    # similar question
    # https://leetcode.com/problems/set-mismatch/description/