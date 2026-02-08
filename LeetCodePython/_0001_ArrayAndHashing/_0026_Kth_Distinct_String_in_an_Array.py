from typing import List
from collections import Counter
from collections import defaultdict
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = defaultdict(int)

        for s in arr:
            count[s] += 1
        
        for s in arr:
            if count[s] == 1:
                k -= 1
            if k == 0:
                return s
        return ""

#====================================================================================================

#   using Counter approach
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = Counter(arr)

        for s in arr:
            if count[s] == 1:
                k -= 1
            if k == 0:
                return s
        return ''

print(Solution().kthDistinct(["d","b","c","b","c","a"], 2))