class Solution:
    def find_buildings(self, heights):
        n = len(heights)
        result = []
        max_height = 0
    
        # Traverse from the last building to the first one
        for i in range(n - 1, -1, -1):
            # If the current building is taller than the max_height, it has an ocean view
            if heights[i] > max_height:
                result.append(i)
                max_height = heights[i]  # Update the max height
        
        # Since we collected results from right to left, reverse them to get the correct order
        return result[::-1]

sol = Solution()
print(sol.find_buildings([4, 2, 3, 1]))