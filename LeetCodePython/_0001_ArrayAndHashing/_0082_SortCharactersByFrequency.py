from typing import Counter
from collections import defaultdict
class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        map = defaultdict(list)

        for ch, cnt in count.items():
            map[cnt].append(ch)
        res = []
        for i in range(len(s), 0, -1):
            if i in map:
                for c in map[i]:
                    res.append(c * i)
        return "".join(res)