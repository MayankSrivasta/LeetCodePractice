from typing import List
class Solution:

#     Input: nums = [3,2,2,3], val = 3
#     Output: 2, nums = [2,2,_,_]

# approach - 1
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

# approach - 2
# To solve this problem using the opposite approach, instead of shifting elements forward, 
# we can remove occurrences of val from the end of the list by swapping elements.
# Opposite Approach: Two-Pointer (Start & End)
# Use two pointers, one from the start (i) and the other from the end (n).
# If nums[i] == val, swap it with nums[n] and decrease n.
# Otherwise, move i forward.
# This avoids unnecessary shifts and works in O(n) time complexity.
 
    def removeElement1(self, nums: List[int], val: int) -> int:
        n = len(nums)  # Track valid length
        i = 0  # Pointer for traversing
        
        while i < n:
            if nums[i] == val:
                nums[i] = nums[n - 1]  # Swap with last valid element
                n -= 1  # Reduce size of valid array
            else:
                i += 1  # Move forward if nums[i] is not val
        
        return n  # Return the new length

Solution().removeElement([0,1,2,2,3,0,4,2], 2)