from typing import List
class Solution:
    # prefix + hashmap  nc
    def minOperations(self, nums: List[int], x: int) -> int:
        total = sum(nums)
        if total == x:
            return len(nums)

        target = total - x
        if target < 0:
            return -1
        
        res = -1
        prefixSum = 0
        prefixMap = {0: -1}  # prefixSum -> index
        
        for i, num in enumerate(nums):
            prefixSum += num
            if prefixSum - target in prefixMap:
                res = max(res, i - prefixMap[prefixSum - target])
            prefixMap[prefixSum] = i
        
        return len(nums) - res if res != -1 else -1

################################################################################################################################################

    # nums = [1,1,4,2,3], x = 5
    # sum = 11
    # 11 - 5 = 6
#   sliding window  nc
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x  # We need to find the longest subarray with sum = target
        cur_sum = 0
        max_window = -1
        l = 0

        for r in range(len(nums)):
            cur_sum += nums[r]

            # if sum is greater than reducing from left side
            # Shrink window from left
            while l <= r and cur_sum > target:
                cur_sum -= nums[l]
                l += 1

            if cur_sum == target:
                max_window = max(max_window, r - l + 1)

             # Min operations = total size - longest subarray
        return -1 if max_window == -1 else len(nums) - max_window
    

# Use a Sliding Window to find the longest subarray whose sum = target.

# Expand the right pointer to increase the sum.

# Shrink the left pointer when the sum exceeds target.