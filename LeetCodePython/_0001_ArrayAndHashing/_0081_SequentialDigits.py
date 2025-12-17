from typing import List
from collections import deque
class Solution:
    # https://neetcode.io/solutions/sequential-digits
    # BFS
    # time complexity - O(1)
    # space complexity - O(1)
    def sequentialDigits2(self, low: int, high: int) -> List[int]:
        res = []
        queue = deque(range(1, 10))
        
        while queue:
            n = queue.popleft()
            if n > high:
                continue
            if low <= n <= high:
                res.append(n)
            ones = n % 10
            if ones < 9:
                queue.append(n * 10 + (ones + 1))
        
        return res
    
    # sliding window approach
    # time complexity - O(1)
    # space complexity - O(1)
    # check LeetCode Python Sheet for step-wise understanding this question
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        nums = "123456789"
        res = []
        for d in range(2, 10):      # d defines the length of the window
            i = 0
            # i + d=only calculates the last no. index so that the last no. shouldn't exceed the limit
            while i + d <= 9:
                num = int(nums[i: i + d])
                if num > high:
                    break
                if low <= num <= high:
                    res.append(num)
                i += 1
        return res
    
    def test1(self):
         for d in range(2, 10):
             print(d)

# print(Solution().sequentialDigits(1000, 13000))

# Overall Complexity
# The function runs in constant time because the maximum number of iterations is fixed (at most 36 iterations).
# Since 36 is a constant, the asymptotic time complexity is: 𝑂(1)
# Thus, even though it looks like O(n^2), it is actually O(1) in practice.
# this is for sliding window

#   AlgoMonster Solution:-
    def sequentialDigitsA(self, low: int, high: int) -> List[int]:
            
            sequential_numbers = []
        
            for start_digit in range(1, 9):    # since 9 cannot start a sequence  
                current_number = start_digit
                for next_digit in range(start_digit + 1, 10):  # Only digits 1-9 are valid
                    current_number = current_number * 10 + next_digit
                    
                    if current_number > high:
                        break
                    if low <= current_number <= high:
                        sequential_numbers.append(current_number)
                    
            return sorted(sequential_numbers)

# Example usage:
solution = Solution()
print(solution.sequentialDigitsA(100, 300))  # Output: [123, 234]

# AlgoMonster solutions Complexity:-
# Sorting Complexity (sorted(res))
# At most 36 numbers are stored in res (since there are only 36 possible sequential numbers).
# Sorting takes O(N log N), where N is the number of valid numbers in the list.
# Since N ≤ 36, sorting is effectively O(1) (constant time) in practical cases.

# in algoMonster solution the approach goes like:-
# 12, 123, 1234, 1235.