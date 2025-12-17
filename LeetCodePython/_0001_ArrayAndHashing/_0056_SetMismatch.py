from collections import Counter
from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = [0, 0] # [duplicate, missing]
        count = Counter(nums)
        for i in range(1, len(nums) + 1):
            if count[i] == 2:
                res[0] = i
            if count[i] == 0:
                res[1] = i
        return res
    
sol = Solution()
print(sol.findErrorNums([1,2,2,4]))

# similar questions
# https://leetcode.com/problems/find-missing-and-repeated-values/