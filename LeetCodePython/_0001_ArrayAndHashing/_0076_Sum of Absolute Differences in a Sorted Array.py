from typing import List

class Solution:
    # using prefix suffix separately for clear understanding:-
    def getSumAbsoluteDifferences(nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        suffix_sum = [0] * (n + 1)
        
        # Compute prefix sums
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        
        # Compute suffix sums
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + nums[i]
        
        # Compute result using precomputed sums
        res = [0] * n
        for i in range(n):
            left = i * nums[i] - prefix_sum[i]
            right = suffix_sum[i + 1] - (n - i - 1) * nums[i]
            res[i] = left + right
        
        return res

# Input: nums = [2,3,5]
# Output: [4,3,5]

    def getSumAbsoluteDifferences1(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n  # Result array
        
        total_sum = sum(nums)  # Sum of all elements
        prefix_sum = 0  # Keeps track of prefix sum
        
        for i, num in enumerate(nums):
            total_sum -= nums[i]  # Remaining sum (excluding nums[i])
            
            left_sum = i * nums[i] - prefix_sum  # Contribution from left elements
            right_sum = total_sum - (n - i - 1) * nums[i]  # Contribution from right elements
            
            res[i] = left_sum + right_sum  # Compute the result for current index
            
            prefix_sum += nums[i]  # Update prefix sum
        
        return res
    
# Final Thoughts
# This prefix sum approach is a common pattern in array transformation problems, 
# reducing brute-force O(n^2) operations to O(n) time.

print(Solution().getSumAbsoluteDifferences1([2,3,5]))