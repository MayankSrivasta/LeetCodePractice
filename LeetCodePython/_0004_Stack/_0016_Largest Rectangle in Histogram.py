from typing import List
class Solution:

# updated NC code with append(0)
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        heights.append(0)
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, v = stack.pop()
                w = i - idx
                maxArea = max(maxArea, v * w)
                start = idx
            stack.append((start, h))
        return maxArea
    
###############################################################################################


    def largestRectangleArea2(self, heights: List[int]) -> int:
        n = len(heights)
        maxArea = 0
        stack = []

        for i in range(n + 1):
            while stack and (i == n  or heights[stack[-1]] >= heights[i]):
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                maxArea = max(maxArea, height * width)
            stack.append(i)
        return maxArea
    
print(Solution().largestRectangleArea([2, 1, 5, 6, 2, 3]))


###############################################################################################