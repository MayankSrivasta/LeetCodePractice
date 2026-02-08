from typing import List
# CHATGPT SOLUTION:-
class NumArray:
    def __init__(self, nums: List[int]):
        self.prefix = [0]
        for num in nums:
            self.prefix.append(self.prefix[-1] + num)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]

# ===========================================================================================================================================

# CHATGPT SOLUTIONS,
class NumArray:

    def __init__(self, nums):
        # Step 1: Build prefix sum
        self.prefix = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.prefix[i+1] = self.prefix[i] + nums[i]
    
    def sumRange(self, left, right):
        # Step 2: Use prefix sums
        return self.prefix[right+1] - self.prefix[left]

# ===========================================================================================================================================

class NumArray:
    #  USING PREFIX SUM APPROACH:-
#                            [-2, 0, 3, -5, 2, -1]
#   prefix sum calculated -> [-2, -2, 1, -4, -2, -3]
#   YOU ARE FUCKING FOOL, GO THROUGH THE VIDEO TO UNDERSTAND THE LOGIC BEHIND 2nd method  
    def __init__(self, nums):
        self.arr = nums[:]  # Copy the input list to avoid modifying the original list
        for i in range(1, len(nums)):
            self.arr[i] += self.arr[i - 1]

    def sumRange(self, left, right):
        if left == 0:
            return self.arr[right]
# GO THROUGH THE VIDEO TO UNDERSTAND THE LOGIN BEHIND THIS LINE    https://neetcode.io/solutions/range-sum-query-immutable    
        return self.arr[right] - self.arr[left - 1]

#       check below example
#                  1     3
#              [1, 3, 6, 10, 15] -> output -> 9
sol = NumArray([1, 2, 3, 4, 5])     
print(sol.sumRange(1, 3))

# WATCH VIDEO FROM 3:13 MIN
#  https://neetcode.io/solutions/range-sum-query-immutable