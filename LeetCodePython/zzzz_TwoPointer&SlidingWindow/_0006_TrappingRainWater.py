from typing import List

class Solution:
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
    
    # easiest approach to understand
    # by creating two different array for leftMax & rightMax
    def trap2(height):
        n = len(height)
        if n <= 2:
            return 0

        left = [0] * n
        right = [0] * n

        left_max = height[0]
        right_max = height[n - 1]

        for i in range(n):
            # Fill left array
            left[i] = left_max = max(left_max, height[i])

            # Fill right array simultaneously (from the end)
            right[n - i - 1] = right_max = max(right_max, height[n - i - 1])

        # Calculate the trapped water
        water = 0
        for i in range(n):
            water += min(left[i], right[i]) - height[i]

        return water

    def trap2(self, height: List[int]) -> int:
        n = len(height)
        i = 0
        j = n - 1
        leftMax = 0
        rightMax = 0
        water = 0
        while(i < j):
            if height[i] < height[j]:
                leftMax = max(leftMax, height[i])
                water += leftMax - height[i]
                i += 1
            else:
                rightMax = max(rightMax, height[j])
                water += rightMax - height[j]
                j -= 1
    
sol = Solution()
print(sol.trap2([0,1,0,2,1,0,1,3,2,1,2,1]))
        

