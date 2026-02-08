from typing import List
import math

class Solution:
    # neetcode.io
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / k)
            if totalTime <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res
    
# 🧠 Why ceil? (The true meaning)
# Because Koko cannot split a single hour across piles.
# So if a pile needs 3.2 hours, she doesn't finish in 3 hours.
# She must take 4 whole hours.
# This is exactly what ceil() does, so for that case also float, needs to be used
# because if we are using int(3.2) which will give = 3, but we want 3.2 & ceil(3.2) = 4