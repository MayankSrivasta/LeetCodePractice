from typing import List
class Solution:
#   Advanced Sliding Window
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        total = 0
        
        for r in range(len(nums)):
            total += nums[r]
            
            if (r - l + 1) * nums[r] > total + k:
                total -= nums[l]
                l += 1

        return len(nums) - l
    
#   ANOTHER MORE UNDERSTANDING APPROACH IS:-
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, total_sum, res = 0, 0, 1
        
        for r in range(len(nums)):
            total_sum += nums[r]
            
            # Check if the current window is invalid
            while (r - l + 1) * nums[r] - total_sum > k:
                total_sum -= nums[l]
                l += 1
            
            # Update the result with the size of the valid window
            res = max(res, r - l + 1)
        
        return res


    
print(Solution().maxFrequency([1, 2, 4,], 5))


# Sliding Window Setup:
# l and r are pointers defining the boundaries of a valid window.

# l tracks the start of the window, and r tracks the end of the window.

# The window [l, r] contains elements that can be incremented to match nums[r] using at most k operations.

# 🔥 Key Observation:
# When the window becomes invalid (i.e., operations needed exceed k), l is moved to the right to reduce the window size.

# After processing all elements, the valid window will be the largest possible window that satisfies the condition.