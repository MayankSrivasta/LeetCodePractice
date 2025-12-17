from typing import List
class Solution:
#  Group Numbers Into Two Arrays :-
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos, neg = [], []
        for num in nums:
            if num > 0:
                pos.append(num)
            else:
                neg.append(num)

        i = 0
#        0  1   2   3  4   5   
#        3, 1, -2, -5, 2, -4
        while 2 * i < len(nums):
            nums[2 * i] = pos[i]
            nums[2 * i + 1] = neg[i]
            i += 1
        return nums
    

    # Two Pointer Approach
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        i, j = 0, 1
        res = [0] * len(nums)
        for k in range(len(nums)):
            if nums[k] > 0:
                res[i] = nums[k]
                i += 2
            else:
                res[j] = nums[k]
                j += 2
        return res