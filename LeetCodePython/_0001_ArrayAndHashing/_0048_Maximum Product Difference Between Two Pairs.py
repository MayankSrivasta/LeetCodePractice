from typing import List
class Solution:
    # APPROACH - 1
    # check from chatgpt for better understanding for approach
    def maxProductDifference(self, nums: List[int]) -> int:
        max1 = max2 = float('-inf') # returns max negative value // # Start with the smallest possible value
        min1 = min2 = float('inf')  # Starts with the largest possible value

        for num in nums:
            if num > max1:
                max2, max1 = max1, num
            elif num > max2:
                max2 = num

            if num < min1:
                min2, min1 = min1, num
            elif num < min2:
                min2 = num

        return (max1 * max2) - (min1 * min2)

#   APPROACH - 2 using sorting approach
# Largest two numbers (nums[-1], nums[-2]) → Used for maximum product.
# Smallest two numbers (nums[0], nums[1]) → Used for minimum product.
    def maxProductDifference2(self, nums: List[int]) -> int:
        nums.sort()
        return nums[-1] * nums[-2] - nums[0] * nums[1]