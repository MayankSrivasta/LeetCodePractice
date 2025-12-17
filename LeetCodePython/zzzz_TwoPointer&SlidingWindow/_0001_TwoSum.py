from typing import List
class Solution:
#  solution -> 1
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val -> index
        for i, v in enumerate(nums):
            diff = target - v
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[v] = i

    def twoSum3(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i, v in enumerate(nums):
            diff = target - v
            if diff in map:
                return [i, map[diff]]
            map[v] = i

# solution -> 2
# using array type data structure
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val -> index
        for i in range(len((nums))):
            diff = target - nums[i]
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[nums[i]] = i