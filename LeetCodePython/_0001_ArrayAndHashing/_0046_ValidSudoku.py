from typing import List
from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # this data structure will be a hashmap in which key will be empty & each key will have empty
        # set attached to it
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                v = board[r][c]
                if v == ".":
                    continue
                if ( v in rows[r]
                    or v in cols[c]
                    or v in squares[(r // 3, c // 3)]):
                    return False

                cols[c].add(v)
                rows[r].add(v)
                squares[(r // 3, c // 3)].add(v)

        return True