from typing import List
class Solution:

#   Approach 2: Using Two Pointers (Space Optimized)
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res
    
#   below is the more easy approach to understand, but the initial intention of solving this question
#   is by using prefix sum, suffix sum approach.
# BELOW CODE MIGHT BE WRONG
    def trap1(self, height: List[int]) -> int:
        n = len(height)
        i = 0
        j = n - 1
        leftMax = 0
        rightMax = 0
        water = 0
        while(i < j):
            leftMax = max(leftMax, height[i])
            rightMax = max(rightMax, height[j])
            water += min(leftMax, rightMax) - height[i]
            i += 1
            j -= 1
        return water

#   Approach 1: Using Dynamic Programming with LeftMax and RightMax Arrays
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0
        
        # Step 1: Create leftMax and rightMax arrays
        leftMax = [0] * n
        rightMax = [0] * n
        
        # Fill leftMax array
        leftMax[0] = height[0]
        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], height[i])
        
        # Fill rightMax array
        rightMax[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i])
        
        # Step 2: Calculate trapped water
        res = 0
        for i in range(n):
            res += min(leftMax[i], rightMax[i]) - height[i]
        
        return res


print(Solution().trap1([0,1,0,2,1,0,1,3,2,1,2,1]))