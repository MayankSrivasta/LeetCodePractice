from typing import List
class Solution:

    # Input: flowerbed = [1,0,0,0,1], n = 1
    # Output: true

    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        f = [0] + flowerbed + [0]
        for i in range(1, len(f) - 1):
            if f[i - 1] == 0 and f[i] == 0 and f[i + 1] == 0:
                f[i] = 1
                n -= 1
        return n <= 0

sol = Solution()
print(sol.canPlaceFlowers([1,0,0,0,1], 1))