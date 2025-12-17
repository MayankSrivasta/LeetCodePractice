from typing import List
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()  # Sort the array to easily find valid pairs
        res = 0
        mod = 10**9 + 7
        
        r = len(nums) - 1  # Pointer at the right end
        
        # Iterate through nums
        for i, left in enumerate(nums):
            # Move the right pointer `r` to the left until sum <= target
            while i <= r and left + nums[r] > target:
                r -= 1
            
            # If a valid subsequence exists
            if i <= r:
                # Add 2^(r - i) subsequences formed between [i, r]
                res += pow(2, r - i, mod)
                res %= mod
        
        return res