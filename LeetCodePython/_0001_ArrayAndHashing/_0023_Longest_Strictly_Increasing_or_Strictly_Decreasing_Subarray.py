from typing import List
class Solution:
    # chatgpt
    def longestStrictlyIncreasingOrDecreasing(self, nums: List[int]) -> int:
        if not nums or len(nums) == 1:
            return len(nums)
        
        inc_len = dec_len = 1
        max_len = 1
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                inc_len += 1
                dec_len = 1  # Reset decreasing
            elif nums[i] < nums[i - 1]:
                dec_len += 1
                inc_len = 1  # Reset increasing
            else:
                inc_len = dec_len = 1  # Reset both if equal
            
            max_len = max(max_len, inc_len, dec_len)
                    
        return max_len

# Related Problems
# Longest Increasing Subarray - LeetCode #674
# Longest Continuous Increasing Subsequence - LeetCode #674
# Find Peak Element - LeetCode #162