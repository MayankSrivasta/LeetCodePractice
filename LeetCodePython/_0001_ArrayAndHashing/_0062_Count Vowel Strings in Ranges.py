from typing import List
class Solution:
    # Category- Range Queries similar to/uses Prefix/Suffix
    # Example Question - Range Sum Query or can search with word Range
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vow = set('aeiou')
        prev = 0
        prefix_count = [0] * (len(words) + 1)
        for i, v in enumerate(words):
            if v[0] in vow and v[-1] in vow:
                prev += 1
            prefix_count[i + 1] += prev

#       since we are using prefix sum so just consider for the time being, we are using [r + 1]
        res = [0] * len(queries)
        for i, q in enumerate(queries):
            l, r = q
            res[i] = prefix_count[r + 1] - prefix_count[l]
        return res