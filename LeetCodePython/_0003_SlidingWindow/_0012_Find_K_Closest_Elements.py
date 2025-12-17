from typing import List
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - 1
        
        # Reduce the window to size k
        while right - left + 1 > k:
            if abs(arr[left] - x) > abs(arr[right] - x):
                left += 1
            else:
                right -= 1
        
        # Return the k closest elements
        return arr[left:right + 1]


print(Solution().findClosestElements([1,2,3,4,5], 4, 3))

# The main objective of the "Find K Closest Elements" problem is to identify the shortest contiguous 
# subarray of length k that contains the elements closest to x.