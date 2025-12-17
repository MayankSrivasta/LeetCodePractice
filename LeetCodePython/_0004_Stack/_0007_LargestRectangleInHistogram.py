from typing import List

# Solution from AlgorithmMadeEasy Youtube
# HARD QUESTION:
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_area = 0
        stack = []
    
        for i in range(n + 1):
            curr_height = 0 if i == n else heights[i]
        
            while stack and curr_height < heights[stack[-1]]:
                top = stack.pop()
                width = i if not stack else i - stack[-1] - 1
                area = heights[top] * width
                max_area = max(area, max_area)
        
            stack.append(i)
    
        return max_area
    
sol = Solution()
print(sol.largestRectangleArea([2, 1, 5, 6, 2, 3]))