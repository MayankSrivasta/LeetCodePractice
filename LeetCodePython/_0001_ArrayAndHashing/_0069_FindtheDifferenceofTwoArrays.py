from typing import List
class Solution:
    # using Hashset
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        num1Set, num2Set = set(nums1), set(nums2)
        res1, res2 = [], []

        for num in num1Set:
            if num not in num2Set:
                res1.append(num)

        for num in num2Set:
            if num not in num1Set:
                res2.append(num)

        return [res1, res2]
    
    # hashset difference
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        numSet1, numSet2 = set(nums1), set(nums2)
        return [list(numSet1 - numSet2), list(numSet2 - numSet1)]