from typing import List
class Solution:

    #   approach - 0 most optimised solution in terms of number of lines of codes
    def gridGame0(self, grid: List[List[int]]) -> int:
        top_sum = sum(grid[0])
        bottom_sum = 0
        result = float('inf')

        for i, v in enumerate(grid[0]):
            top_sum -= v
            result = min(result, max(top_sum, bottom_sum))
            bottom_sum += grid[1][i]
        return result    

#====================================================================================================

    # approach - 1
    def gridGame(self, grid: List[List[int]]) -> int:
        N = len(grid[0])
        preRow1, preRow2 = grid[0].copy(), grid[1].copy()

        for i in range(1, N):
            preRow1[i] += preRow1[i - 1]
            preRow2[i] += preRow2[i - 1]

        res = float("inf")
        for i in range(N):
            top = preRow1[-1] - preRow1[i]
            bottom = preRow2[i - 1] if i > 0 else 0
            secondRobot = max(top, bottom)
            res = min(res, secondRobot)
        return res

#====================================================================================================

    # approach - 2      Neetcode.io PrefixSum Space Optimized
    def gridGame2(self, grid: List[List[int]]) -> int:
        res = float("inf")
        topSum = sum(grid[0])
        bottomSum = 0

        for i in range(len(grid[0])):
            topSum -= grid[0][i]
            res = min(res, max(topSum, bottomSum))
            bottomSum += grid[1][i]

        return res
    
#====================================================================================================

    # approach - 3
    def gridGame3(self, grid: List[List[int]]) -> int:
        sum_top = sum(grid[0]) - grid[0][0]
        sum_bottom = 0
        res = max(sum_top, sum_bottom)

        for partition in range(1,len(grid[0])):
            sum_top -= grid[0][partition]
            sum_bottom += grid[1][partition-1]
            res = min(res, max(sum_top, sum_bottom))
        return res

#====================================================================================================

    # solution from AlgoMaster website      https://algo.monster/liteproblems/2017
    # this one has minimum number of lines of codes
    def gridGame(self, grid: List[List[int]]) -> int:
        # Initialize the answer to an infinite value since we want to minimize it later
        min_max_score = float('inf')
      
        # Sum of the top row's elements
        top_sum = sum(grid[0])
        # Initialize bottom sum to 0 since the robot hasn't moved yet
        bottom_sum = 0
      
        # Iterate through the elements of the top row
        for index, value in enumerate(grid[0]):
            # Robot moves down, so remove the current value from the top row sum
            top_sum -= value
            # Calculate the maximum of the remaining sums after removing the current column
            min_max_score = min(min_max_score, max(top_sum, bottom_sum))
            # Add the current value from the bottom row to its sum as the robot can take it
            bottom_sum += grid[1][index]
      
        # Return the minimum value found among the maximum sums after each possible move
        return min_max_score