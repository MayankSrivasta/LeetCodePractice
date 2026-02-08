from typing import List
from collections import Counter
class Solution:

    # Requirement it needs to be solved in time O(n) & space O(1)

    # using hashmap ->
    # time complexity -> O(n)
    # space complexity -> O(n)
    def findDuplicates(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        res = []

        for num in count:
            if count[num] == 2:
                res.append(num)
        
        return res
#====================================================================================================
    
    # negative marking approach - neetcode.io
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []

        for num in nums:
            idx = abs(num) - 1
            if nums[idx] < 0:
                res.append(abs(num))
            nums[idx] = -nums[idx]
        
        return res
#====================================================================================================
    
# the approach for this solution is simple:-
# in case 3 3 2 2
# first we get 3, we get the index as 2, we make value at index
# 2 as -ve, so that in case if again 3 comes in the given array,
# we can directly reach to the index & check what's its value is
# if its -ve then it means that we have already visited it else
# we make it -ve. -> check register for diagram