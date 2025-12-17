from typing import List

class Solution:
    # chatgpt
#   We iterate through the array and count how many times the order decreases (drops).
#   Additionally, the last element should not be greater than the first, ensuring a valid rotation.

# Time Complexity: O(n) (Single pass)
# Space Complexity: O(1) (Constant space)

    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        count = 0  # Count of decreasing pairs
        
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:  # Compare current with next (circular)
                count += 1
            
            if count > 1:
                return False  # More than 1 drop, not sorted & rotated
        
        return True  # At most 1 drop, valid sorted and rotated array
    

# chatgpt - 1
def check(nums: List[int]) -> bool:
    count = 0
    for i in range(1, len(nums)):
        if nums[i-1] > nums[i]:
            count += 1
    # plus check wrap-around
    if nums[-1] > nums[0]:
        count += 1
    return count <= 1
