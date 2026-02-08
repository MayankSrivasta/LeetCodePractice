from typing import List
class Solution:

    # Brute Force
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums) - 1):
            sum = nums[i]
            for j in range(i + 1, len(nums)):
                sum += nums[j]
                if sum % k == 0:
                    return True
        return False

#====================================================================================================

    # HashMap + Prefix Sum
    # go through video 10:30 min to understand the edge case {0 : -1}
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder = {0: -1}  # remainder -> end index
        total = 0

        for i, num in enumerate(nums):
            total += num
            r = total % k
            if r not in remainder:
                remainder[r] = i
            elif i - remainder[r] > 1:
                return True
        
        return False