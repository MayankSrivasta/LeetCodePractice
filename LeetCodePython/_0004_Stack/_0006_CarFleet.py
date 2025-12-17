from typing import List

"""
Intuition:
Sort cars by starting position (farthest to closest to the target).
Because the cars ahead can block the cars behind.
For each car:
Calculate time needed to reach the target: (target - pos) / speed
Use a stack:
If a car takes more time than the car ahead (top of stack), it forms a new fleet → push.
If it takes less or equal time, it joins the existing fleet → don't push.
"""
class Solution:

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        for p, s in pair:  # Reverse Sorted Order
            val = (target - p) / s
            stack.append(val)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
    
    def carFleet2(self, target : int, position : List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse = True)
        stack = []
        for p, s in pair:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
            




#  input -> target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
#  output -> 3
sol = Solution()
print(sol.carFleet2(12, [10,8,0,5,3], [2,4,1,1,3]))