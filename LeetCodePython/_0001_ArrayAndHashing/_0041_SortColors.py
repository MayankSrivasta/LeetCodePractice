from typing import List
from collections import Counter
class Solution:

    # approach - 1  Three Pointers - III neetcode.io solution
    def sortColors1(self, nums: List[int]) -> None:
        zero = one = 0
        for i in range(len(nums)):
            tmp = nums[i]  # Store the original value
            if tmp < 2:
                nums[one] = 1
                one += 1
            if tmp < 1:
                nums[zero] = 0
                zero += 1
            nums[i] = 2  # Now assign 2 at the correct position

#====================================================================================================

#   using Counter approach for reducing code from above solution
    def sortColors(self, nums: List[int]) -> None:
        count = Counter(nums)  # Count occurrences of 0, 1, and 2
        
        index = 0
        for i in range(3):  # Colors are 0, 1, 2
            for _ in range(count[i]):  # Place each number `count[i]` times
                nums[index] = i
                index += 1

    # COUNTING SORT/ FREQUENCY COUNT APPROACH
        count = [0] * 3
        for num in nums:
            count[num] += 1

            # for above 2 lines u can also use Counter
        
        index = 0
        for i in range(3):
            while count[i]:
                count[i] -= 1
                nums[index] = i
                index += 1

#====================================================================================================

#   Dutch National Flag Algorithm - Best Solution for it.
    def sortColors(self, nums: List[int]) -> None:
        low, mid, high = 0, 0, len(nums) - 1
        
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:  # nums[mid] == 2
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1


sol = Solution()
sol.sortColors1([2,0,2,1,1,0])

#====================================================================================================

# Bonus 🧠 — Mapping to LeetCode Patterns

# This problem introduces you to:

# ✔ Counting sort (Counter)
# ✔ Bucket frequency (like Top K elements)
# ✔ 3-way partitioning (DNF)
# ✔ Prefix patterns (indirectly when k > 3)