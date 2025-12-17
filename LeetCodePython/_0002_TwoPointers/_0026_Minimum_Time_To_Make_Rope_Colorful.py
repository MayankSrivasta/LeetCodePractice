from typing import List
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        l = 0
        res = 0
        for r in range(1, len(colors)):
            if colors[l] == colors[r]:
                res += min(neededTime[l], neededTime[r])
                l = r if neededTime[r] > neededTime[l] else l
            else:
                l = r
        return res