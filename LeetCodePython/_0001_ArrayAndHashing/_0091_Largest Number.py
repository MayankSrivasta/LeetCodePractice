from functools import cmp_to_key
from typing import List

class Solution:
    # copilot solution
    def largestNumber(self, nums):
        def compare(x, y):
            # Custom comparator to decide the order
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0

        # Convert numbers to strings for comparison
        nums = list(map(str, nums))
        # Sort using the custom comparator
        nums.sort(key=cmp_to_key(compare))
        # Join the sorted numbers
        result = ''.join(nums)
        # Handle the case where the result is all zeros
        return '0' if result[0] == '0' else result

#   NeetCode solution
    def largestNumber(self, nums: List[int]) -> str:
            for i, n in enumerate(nums):
                 nums[i] = str(n)

            def comp(n1, n2):
                 if n1 + n2 > n2 + n1:
                      return -1
                 else:
                      return 1
            nums = sorted(nums, key=cmp_to_key(comp))
            # Handle the case where the result is all zeros
            # "000" -> "0"
            return str(int("".join(nums)))
    

# Example usage
if __name__ == "__main__":
    solution = Solution()
    nums = [3, 30, 34, 5, 9]
    print(solution.largestNumber(nums))  # Output: "9534330"