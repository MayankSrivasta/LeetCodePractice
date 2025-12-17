from typing import List

class Solution:
    # approach - 1 go through neetcode video - 6:30 min to understand properly
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left, right = 1, 1
        n = len(nums)
        arr = [1] * n  # Initialize array with 1s
        
        for i in range(n):
            arr[i] = left
            left *= nums[i]

        for i in range(n - 1, -1, -1):
            arr[i] *= right
            right *= nums[i]

        return arr


sol = Solution()
print(sol.productExceptSelf([1, 2, 3, 4]))  
# Output: [24, 12, 8, 6]