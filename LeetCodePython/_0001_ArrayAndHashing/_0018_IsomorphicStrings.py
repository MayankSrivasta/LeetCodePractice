

# similar as ques-21 word pattern

# for this question you just have to manage & check in both the strings, the character in s string
#  should be mapped  to t character in t string and t character in t string should be mapped to s character in s string.

class Solution:

# Isomorphic -> Two strings s and t are isomorphic if the characters in s can be replaced to get t.

    # Input: s = "egg", t = "add"
    # Output: true

    def isIsomorphic(self, s: str, t: str) -> bool:
        sMap, tMap = {}, {}
        for i in range(len(s)):
            schar, tchar = s[i], t[i]
            if((schar in sMap and sMap[schar] != tchar) or (tchar in tMap and tMap[tchar] != schar)):
                return False
            sMap[schar] = tchar
            tMap[tchar] = schar
        return True

#====================================================================================================

#   solving using zip is much more efficient, logically easy to understand
    def isIsomorphic(self, s: str, t: str) -> bool:
        sMap, tMap = {}, {}

        for schar, tchar in zip(s, t):  # Unpack characters directly
            if (schar in sMap and sMap[schar] != tchar) or (tchar in tMap and tMap[tchar] != schar):
                return False
            sMap[schar] = tchar
            tMap[tchar] = schar

        return True