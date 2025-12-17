class Solution:
    # neetcode.io
    # time complexity is same O(n) but this one take space complexity as O(n)
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                skipL = s[l + 1 : r + 1]
                skipR = s[l : r]
                return skipL == skipL[::-1] or skipR == skipR[::-1]
            l, r = l + 1, r - 1

        return True
    
    # doesn't take space complexity O(n)
    def validPalindrome(self, s: str) -> bool:
        def test(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return test(l + 1, r) or test(l, r - 1)
            l += 1
            r -= 1
        return True
    
print(Solution().validPalindrome("abbc"))