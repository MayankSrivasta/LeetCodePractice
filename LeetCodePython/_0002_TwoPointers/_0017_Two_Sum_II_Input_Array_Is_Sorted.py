from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]

            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1]
        return []
    
#========================================================================================================= 

    # the reason for writing this one is to learn the of writing the code ->  res += [l + 1, r + 1]
    def twoSum(self, num: List[int], target: int) -> List[int]:
        l, r = 0, len(num) - 1
        res = []
        while l < r:
            sum = num[l] + num[r]
            if sum < target:
                l += 1
            elif sum > target:
                r -= 1
            else:
                res += [l + 1, r + 1]
                return res
        return res