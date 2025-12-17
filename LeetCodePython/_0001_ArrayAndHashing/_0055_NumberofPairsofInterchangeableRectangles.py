from typing import List
class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        count = {}
        for w, h in rectangles:
            count[w / h] = 1 + count.get(w / h, 0)

        res = 0

    # This is the formula for counting the number of ways to choose two elements from a group of
    # N elements, which is also known as the combinations formula:

        for c in count.values():
            if c > 1:
                res += (c * (c - 1)) // 2
        return res