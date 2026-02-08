from typing import List
class Solution:

# CODING INTERVIEW PATTERN book also have this question. - read that for better understanding.
# chatgpt solution:-
    def search(self, nums, target):
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r)//2
            
            if nums[mid] == target:
                return mid
            
            # left sorted
            if nums[l] <= nums[mid]:
                # If target lies in this sorted left:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
                    
            # right sorted
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1

############################################################################################

# neetcode solution

    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            
            # left sorted portion 
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            
            # right sorted portion
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1