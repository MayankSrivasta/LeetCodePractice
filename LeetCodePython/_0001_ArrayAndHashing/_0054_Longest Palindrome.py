class Solution:
    def longestPalindrome(self, s: str) -> int:
        res = 0
        seen = set()
        for c in s:
            if c in seen:
                seen.remove(c)
                res += 2
            else:
                seen.add(c)
        return res + 1 if seen else res
        