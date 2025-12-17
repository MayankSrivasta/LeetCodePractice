from typing import List

class Solution:
    # monotonic decreasing
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        results = [0] * len(temps)
        stack = []

        for i, temp in enumerate(temps):
            while stack and temps[stack[-1]] < temp:
                index = stack.pop()
                results[index] = i - index
            stack.append(i)

        return results
    
sol = Solution()
# print(sol.dailyTemperatures([73,74,75,71,69,72,76,73]))

# while condition is required for below inputs, where we have monotonic decreasing values, so it just keeps 
# on checking whether we get any higher value than current value
# print(sol.dailyTemperatures([9,8,7,6,5,4,3,2,1,10]))