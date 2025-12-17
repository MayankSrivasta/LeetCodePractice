from typing import List
from collections import defaultdict
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        count = defaultdict(int)
        res = []

        for num in nums:
            row = count[num]
            if len(res) == row:
                res.append([])
            res[row].append(num)
            count[num] += 1

        return res