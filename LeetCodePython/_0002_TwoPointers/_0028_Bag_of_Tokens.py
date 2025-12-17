from typing import List
class Solution:

#   Greedy + Two Pointers
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        res = score = 0
        tokens.sort()
        l, r = 0, len(tokens) - 1
        while l <= r:
            if power >= tokens[l]:
                power -= tokens[l]
                l += 1
                score += 1
                res = max(res, score)
            elif score > 0:
                power += tokens[r]
                r -= 1
                score -= 1
        #   3rd case -> when we don't have enough power to play a token & we also have a score of 0,
        #   so we can't play to token to play down, in that case we should just return
            else:
                break
        return res