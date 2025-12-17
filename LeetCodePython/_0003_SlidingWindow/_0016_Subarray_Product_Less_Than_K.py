from typing import List
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        res = 0
        l = 0
        product = 1
        for r in range(len(nums)):
            product *= nums[r]
            while l <= r and product >= k:
                product //= nums[l]
                l += 1
#       so the main logic for below line to consider the length as the subarray is that,
#       since the product of suppose 2-length subarray is less than 100, then like 5*2 < 100, 
#       then [5, 2] & [5] is an subarray check https://neetcode.io/solutions/subarray-product-less-than-k
#       video from 6:00 minutes
            res += (r - l + 1)
        return res

print(Solution().numSubarrayProductLessThanK([10,5,2,6], 100))