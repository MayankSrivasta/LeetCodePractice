from typing import List

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rightMax = -1  # Initialize rightMax to -1 (as required by the problem)

        for i in range(len(arr) - 1, -1, -1):
            newMax = max(arr[i], rightMax)
            arr[i] = rightMax
            rightMax = newMax

        return arr