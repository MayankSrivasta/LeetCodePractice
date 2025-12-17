from typing import List
class Solution:
#   solving by two pointer approach
    def firstPalindrome(self, words: List[str]) -> str:
        for w in words:
            l = 0
            r = len(w) - 1
            while w[l] == w[r]:
                if l >= r:
                    return w
                l += 1
                r -= 1
        return ""

#   solving by reversing the string
    def firstPalindrome(self, words: List[str]) -> str:
        for w in words:
            if w == w[::-1]:
                return w
        return ""