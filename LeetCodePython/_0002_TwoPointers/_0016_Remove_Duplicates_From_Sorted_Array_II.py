from typing import List
class Solution:
    # two pointers approach
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0       # keep track of the position to insert a valid element.
        for num in nums:
            if l < 2 or num != nums[l - 2]:
                nums[l] = num
                l += 1
        return l
    
    def removeDuplicates1(self, nums: List[int]) -> int:
        i = 2
        for j in range(2, len(nums)):
            if nums[i - 2] != nums[j]:
                nums[i] = nums[j]
                i += 1
        return i
    

print(Solution().removeDuplicates([0,0,0,0,1,1,1,1,2,3,3]))