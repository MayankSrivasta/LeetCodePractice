from collections import Counter
class Solution:
    # first and last index approach
    # this approach goes from sides to mid to calculate the characters
    def countPalindromicSubsequence(self, s: str) -> int:
        res = 0
        for i in range(26):
            c = chr(ord('a') + i)
            l, r = s.find(c), s.rfind(c)
            if l == -1 or l == r:
                continue
            
            mids = set()
            for j in range(l + 1, r):
                mids.add(s[j])
            res += len(mids)

        return res
    

    #  s.find(c) or rfind(c) returns -1 incase if a character is not found

#   iterate on Middle Character
#   this approach goes from mid to sides to calculate the characters
    def countPalindromicSubsequence(self, s: str) -> int:
        res = set()
        left = set()
        right = Counter(s)
        
        for i in range(len(s)):
            right[s[i]] -= 1
            if right[s[i]] == 0:
                right.pop(s[i])
            
            for j in range(26):
                c = chr(ord('a') + j)
                if c in left and c in right:
                    res.add((s[i], c))
            left.add(s[i])
            
        return len(res)