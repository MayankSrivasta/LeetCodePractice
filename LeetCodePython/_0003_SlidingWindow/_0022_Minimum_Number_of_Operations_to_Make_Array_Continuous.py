from typing import List
class Solution:
    # sliding window
    # time complexity - O(nlogn)
    # space complexity - O(n)

    # https://youtu.be/4G8puv5PcV0
    # check the above video from 8:30 minutes to understand better.
    def minOperations(self, nums: List[int]) -> int:
        length = len(nums)
        nums = sorted(set(nums))
        res = length
        r = 0

        for l in range(len(nums)):
            while r < len(nums) and nums[r] < nums[l] + length:
                r += 1
            window = r - l
            res = min(res, length - (r - l))

        return res
    
    # sliding window - optimal
    # time complexity - O(nlogn)
    # space complexity - O(n)
    def minOperations(self, nums: List[int]) -> int:
        length = len(nums)
        nums.sort()
        res = length
        n = 1

        for i in range(1, length):
            if nums[i] != nums[i - 1]:
                nums[n] = nums[i]
                n += 1
        
        l = 0
        for r in range(n):
            l += (nums[r] - nums[l] > length - 1)

        return length - (n - l)