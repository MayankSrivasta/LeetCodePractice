from typing import List

# APPROACH - 1
# using 2 separate arrays

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        prefix = [1] * n
        suffix = [1] * n
        result = [1] * n

        # Build prefix array
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        # Build suffix array
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        # Build result
        for i in range(n):
            result[i] = prefix[i] * suffix[i]

        return result

# =============================================================================================

# APPROACH - 2

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


