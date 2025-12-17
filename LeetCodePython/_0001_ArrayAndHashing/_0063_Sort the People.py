from typing import List
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        height_name = {}
        for h, n in zip(heights, names):
            height_name[h] = n
        
        res = []
        for h in reversed(sorted(height_name)):
            res.append(height_name[h])
        return res
