from typing import List
class Solution:
    # testing with list -> [3, 4, 2, 5]
#  reverse traversal order   -> chatgpt solution
    def checkPossibility(self, nums: List[int]) -> bool:
        modified = False  # Boolean flag to track if a modification was made
        
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:  # Found a violation
                if modified:  # If we already modified once, return False
                    return False
                
                modified = True  # Mark modification as used
                
                # Modify nums[i] or nums[i+1] appropriately
                if i == 0 or nums[i - 1] <= nums[i + 1]:
                    nums[i] = nums[i + 1]  # Lower nums[i] to nums[i+1]
                else:
                    nums[i + 1] = nums[i]  # Raise nums[i+1] to nums[i]

        return True  # Array can be made non-decreasing with at most one modification

#====================================================================================================

# testing with list -> [3, 4, 2, 5]
# forward traversal approach       -> chatgpt solution
    def checkPossibility(self, nums: List[int]) -> bool:
        modified = False  # Boolean flag to track if a modification was made
        
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:  # Found a violation
                if modified:  # If we already modified once, return False
                    return False
                
                modified = True  # Mark modification as used
                
                # Modify nums[i] or nums[i+1] appropriately
                if i == 0 or nums[i - 1] <= nums[i + 1]:
                    nums[i] = nums[i + 1]  # Lower nums[i] to nums[i+1]
                else:
                    nums[i + 1] = nums[i]  # Raise nums[i+1] to nums[i]

        return True  # Array can be made non-decreasing with at most one modification

#====================================================================================================

# testing with list -> [3, 4, 2, 5]
# NeetCode.io solution
    def checkPossibility2(self, nums: list[int]) -> bool:
        changed = False

        for i in range(len(nums) - 1):
            if nums[i] <= nums[i + 1]:
                continue
            if changed:
                return False
            if i == 0 or nums[i - 1] <= nums[i + 1]:
                nums[i] = nums[i + 1]
            else:
                nums[i + 1] = nums[i]
            changed = True
        return True
    
print(Solution().checkPossibility2([1,2,3]))