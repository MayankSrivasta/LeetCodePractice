from typing import List
class Solution:
    # from NeetCode.io  Greedy Approach
    def wiggleSort(self, nums: List[int]) -> None:
        for i in range(1, len(nums)):
            if ((i % 2 == 1 and nums[i] < nums[i - 1]) or
                (i % 2 == 0 and nums[i] > nums[i - 1])):
                nums[i], nums[i - 1] = nums[i - 1], nums[i]
        return nums
    # [3, 5, 1, 6, 2, 4]

    def wiggleSortSelf(self, nums: List[int]) -> None:
        for i in range(1, len(nums)):
            if ((i % 2 == 1 and nums[i] < nums[i - 1]) or
            (i % 2 == 0 and nums[i] > nums[i - 1])):
                nums[i], nums[i - 1] = nums[i - 1] , nums[i]
        return nums
    
print(Solution().wiggleSortSelf([3, 5, 2, 1, 6, 4]))
# output -> [1, 6, 2, 5, 3, 4]