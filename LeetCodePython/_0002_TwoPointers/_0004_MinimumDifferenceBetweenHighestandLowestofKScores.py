from typing import List
class Solution:
    # intitution:-
    # to get the min. difference is to have the nos. which are most adjacent to each other in terms of values

    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = float('inf')
        l = 0
        r = k - 1
        while r < len(nums):
            res = min(res, nums[r] - nums[l])
            r += 1
            l += 1
        return res