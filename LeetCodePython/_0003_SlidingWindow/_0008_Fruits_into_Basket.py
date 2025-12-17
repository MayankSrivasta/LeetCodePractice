from typing import List
from collections import defaultdict
class Solution:
#   find the longest contigious subarray that has atmost 2 distinct fruits
    def totalFruit(self, fruits: List[int]) -> int:
        count = defaultdict(int)
        l = 0
        res = 0
        for r in range(len(fruits)):
            count[fruits[r]] += 1

            if len(count) > 2:
                count[fruits[l]] -= 1
                if count[fruits[l]] == 0:
                    count.pop(fruits[l])
                l += 1
        
            res = max(res, r - l + 1)
        return res

print(Solution().totalFruit([0,1,2,2]))