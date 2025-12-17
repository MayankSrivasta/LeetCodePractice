from typing import List
class Solution:

    # Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
    # Output: [-1,3,-1]

#   approach - 1  TO UNDERSTAND THIS APPROACH DEBUG IT 
#   complexity O(n + m)
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []  # Monotonic decreasing stack
        next_greater = {}  # Dictionary to store the next greater element for each number in nums2

        # Traverse nums2 from right to left
        for num in reversed(nums2):
            while stack and stack[-1] <= num:
                stack.pop()  # Remove smaller or equal elements
            next_greater[num] = stack[-1] if stack else -1  # Store next greater element or -1
            stack.append(num)  # Push current element onto the stack

        # Map results for nums1 based on nums2
        return [next_greater[num] for num in nums1]
    

# without comments easy to understand
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        map = {}
        for i in range(len(nums2)):
            map[nums2[i]] = -1
            for j in range(i + 1, len(nums2)):
                if nums2[i] < nums2[j]:
                    map[nums2[i]] = nums2[j]
                    break
        
        return [map[num] for num in nums1]
        
# same code as above just with comments
    # using HASHMAP
    # O(n2)
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {}  # HashMap to store next greater elements
        
        # Precompute next greater elements for all numbers in nums2
        for i in range(len(nums2)):
            next_greater[nums2[i]] = -1  # Default value if no greater element is found
            for j in range(i + 1, len(nums2)):  # Look for the next greater element
                if nums2[j] > nums2[i]:
                    next_greater[nums2[i]] = nums2[j]
                    break  # Stop at the first greater element

        # Lookup results for nums1
        return [next_greater[num] for num in nums1]

sol = Solution()
print(sol.nextGreaterElement([4,1,2], [1,3,4,2]))