from typing import List
class Solution:
    # time - O(n)
    # space - O(n)
    
    # approach - 1
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        tmp = [0] * n
        for i in range(n):
            tmp[(i + k) % n] = nums[i]
        
        nums[:] = tmp


# approach - 2
#   Reversal Traversal
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n

        def reverse(l: int, r: int) -> None:
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l, r = l + 1, r - 1

        reverse(0, n - 1)   # Reverse entire array
        reverse(0, k - 1)   # Reverse first k elements
        reverse(k, n - 1)   # Reverse remaining elements

# approach - 3
    
    # time - O(n)
    # space - O(n)
#   the above Reversal Approach can be done using Pythonic Slicing Approch:-
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n  # Handle cases where k >= n

        # Reverse entire array
        nums[:] = nums[::-1]
        
        # Reverse first k elements
        nums[:k] = nums[:k][::-1]
        
        # Reverse remaining elements
        nums[k:] = nums[k:][::-1]

# approach - 4
    # time - O(n)
    # space - O(1)
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n  # Handle cases where k >= n

        # Reverse entire array
        nums[:] = reversed(nums)

        # Reverse first k elements
        nums[:k] = reversed(nums[:k])

        # Reverse remaining elements
        nums[k:] = reversed(nums[k:])


# ⚡️ Key Difference Between [::-1] and reversed():
# [::-1] creates a new list in reverse order.

# reversed() returns a reverse iterator that can be used to modify the list in place.

# ✅ Both approaches are valid, but reversed() is considered more memory efficient since 
# it doesn’t create a new list if used with nums[:].