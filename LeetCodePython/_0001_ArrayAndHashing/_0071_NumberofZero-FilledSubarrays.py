from typing import List
class Solution:
#   debug it there is a trick u need to understand how it is calculating the res
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res = count = 0
        for n in nums:
            if n == 0:
                count += 1
            else:
                count = 0
            res += count
        return res
        
Solution().zeroFilledSubarray([1,3,0,0,2,0,0,4])