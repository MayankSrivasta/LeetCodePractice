from typing import List
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum = rightSum = 0
        totalSum = sum(nums)

        for i in range(len(nums)):
            rightSum = totalSum - leftSum - nums[i]
            if rightSum == leftSum:
                return i
            leftSum += nums[i]
        return -1
        