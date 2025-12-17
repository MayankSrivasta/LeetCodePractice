from typing import List
class Solution:
    # shortcut approach for writing 2nd FOR loop
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)

        for X in range(1, n + 1):  # X can be between 1 and len(nums)
            count = sum(1 for num in nums if num >= X)
            if count == X:
                return X
        
        return -1  # No valid X found

# approach - 2

class Solution:
    # using 2 full for loop
    def specialArray2(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)

        for X in range(1, n + 1):
            count = 0
            for num in nums:
                if num >= X:
                    count += 1
            if count == X:
                return X
        
        return -1  # No valid X found

# approach - 3  COUNTING SORT - neetcode.io     BEST SOLUTION:->
    def specialArray(self, nums: List[int]) -> int:
        count = [0] * (len(nums) + 1)
        for num in nums:
            index = min(num, len(nums))
            count[index] += 1

        total_right = 0
        for i in range(len(nums), -1, -1):
            total_right += count[i]
            if i == total_right:
                return total_right
        return -1