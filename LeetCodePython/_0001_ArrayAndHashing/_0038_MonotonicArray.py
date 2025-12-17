from typing import List

class Solution:
    # APPROACH - 1
    def isMonotonic(self, nums: List[int]) -> bool:
            increase, decrease = True, True
            for i in range(len(nums) - 1):
                if not (nums[i] <= nums[i + 1]):
                    increase = False
                if not (nums[i] >= nums[i + 1]):
                    decrease = False
            return increase or decrease
    
    # APPROACH - 2    
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing, decreasing = True, True
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                decreasing = False
            if nums[i] > nums[i + 1]:
                increasing = False
        return increasing or decreasing


sol = Solution()
print(sol.isMonotonic([1,2,2,3]))
print(sol.isMonotonic([6,5,4,4]))
print(sol.isMonotonic([1,3,2]))