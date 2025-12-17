from typing import List
class Solution:

    # Input: flowerbed = [1,0,0,0,1], n = 1
    # Output: true

    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        temp = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed) - 1):
            if temp[i - 1] == 0 and temp[i] == 0 and temp[i + 1] == 0:
                temp[i] = 1
                n -= 1
        return n == 0

sol = Solution()
print(sol.canPlaceFlowers([1,0,0,0,1], 1))