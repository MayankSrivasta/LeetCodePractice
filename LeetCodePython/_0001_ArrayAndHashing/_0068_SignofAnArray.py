from typing import List    

class Solution:
    # tracking sign of the product
    def arraySign(self, nums: List[int]) -> int:
        sign = 1
        for n in nums:
            if n == 0:
                return 0
            if n < 0:
                sign *= -1
        return sign