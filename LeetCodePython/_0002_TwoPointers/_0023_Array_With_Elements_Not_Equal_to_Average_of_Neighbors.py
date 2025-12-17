from typing import List
class Solution:
    # O(nlogn)
    # space - O(n)
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = []
        l, r = 0, len(nums) - 1
        while len(res) != len(nums):
            res.append(nums[l])
            l += 1
            # if below line is not added then the middle element will be added twice in case of odd numbers
            if l <= r:
                res.append(nums[r])
                r -= 1
        return res
    

    #   O(n)
    #   O(1) extra space
    def rearrangeArray2(self, nums: List[int]) -> List[int]:
        increase = nums[0] < nums[1]
        for i in range(1, len(nums) - 1):
            if ((increase and nums[i] < nums[i + 1]) or
                (not increase and nums[i] > nums[i + 1])
            ):
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
            increase = not increase
        return nums
    
print(Solution().rearrangeArray())



# Sorting Trick:
# If you sort the array and interleave smaller and larger elements, you can prevent the average condition from being met.
# Divide the sorted array into 2 halves:
# Left Half: Smaller elements.
# Right Half: Larger elements.
# Place elements by taking one from the right half and one from the left half alternately.

#  Optimal Approach:
# ✨ Intuition:
# By placing larger and smaller elements alternately, you avoid the situation where an element becomes the average of its neighbors.
# Interleaving Pattern:
# Place the largest half in even indices.
# Place the smallest half in odd indices.