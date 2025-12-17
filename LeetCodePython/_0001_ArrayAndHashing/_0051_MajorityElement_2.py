from typing import List
from collections import Counter
class Solution:
    
    # Time Complexity = O(N) & Space Complexity = O(N) 
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        res = []

        for key in count:
            if count[key] > len(nums) // 3:
                res.append(key)
        
        return res
    
    # solve the problem in linear time and in O(1) space?
    # https://neetcode.io/solutions/majority-element-ii

