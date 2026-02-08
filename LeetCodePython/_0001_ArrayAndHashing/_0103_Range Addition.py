# premium leetcode problem
# https://leetcode.com/problems/range-addition/
from typing import List
"""
You are given an integer length and an array updates where updates[i] = [startIdxi, endIdxi, inci].

You have a 0-indexed array arr of length length with all zeros. For each updates[i], increment all arr[startIdxi], arr[startIdxi + 1], ..., arr[endIdxi] by inci.

Return arr after applying all the updates.

Example 1:
Input: length = 5, updates = [[1,3,2],[2,4,3],[0,2,-2]]
Output: [-2,0,3,5,3]

Example 2:
Input: length = 10, updates = [[2,4,6],[5,6,8],[1,9,-4]]
Output: [-4,-4,-2,2,2,4,4,-4,-4,-4]

Constraints:
1 <= length <= 105
0 <= updates.length <= 104
0 <= startIdxi <= endIdxi < length
-1000 <= inci <= 1000
"""

class Solution:
    #  chatgpt
    def getModifiedArray(self, n: int, updates: List[List[int]]) -> List[int]:
        diff = [0] * (n + 1)  # One extra space to handle the (end + 1) index

        # Apply difference-style range updates
        for start, end, val in updates:
            diff[start] += val
            if end + 1 < len(diff):
                diff[end + 1] -= val

        # Apply prefix sum to get final values
        res = [0] * n
        curr = 0
        for i in range(n):
            curr += diff[i]
            res[i] = curr

        return res


print(Solution().getModifiedArray(5, ([[1, 3, 2], [2, 4, 3], [0, 2, -2]])))
# Output: [-2, 0, 3, 5, 3]

#====================================================================================================

# Explanation:
# Initial state: [0, 0, 0, 0, 0]
# After applying the first update [1, 3, 2]: [0, 2, 2, 2, 0]
# After applying the second update [2, 4, 3]: [0, 2, 5, 5, 3]
# After applying the third update [0, 2, -2]: [-2, 0, 3, 5, 3]
# The final array is [-2, 0, 3, 5, 3]

# The difference array technique is used to efficiently apply RANGE UPDATES.
# The time complexity is O(n + m), where n is the length of the array and m is the number of updates.
# The space complexity is O(n) for the difference array.
# The difference array technique allows us to perform range updates in constant time.
# The prefix sum is then used to compute the final values in linear time.
# The algorithm is efficient and works well for large inputs.
# The solution is optimal and has a time complexity of O(n + m), where n is the length of the array and m is the number of updates.
# The space complexity is O(n) for the difference array.