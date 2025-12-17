from typing import List
class Solution:
    # https://leetcode.com/problems/concatenation-of-array/description/
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        arr = [0] * (n * 2)
        for i in range(n):
            arr[i] = nums[i]
            arr[i + n] = nums[i]
        return arr


# Input: nums = [1,2,1]
# Output: [1,2,1,1,2,1]