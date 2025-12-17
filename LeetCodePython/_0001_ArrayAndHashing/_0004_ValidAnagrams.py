from typing import List
from collections import defaultdict
from collections import Counter


class Solution:
                            # "anagram", "nagaram"
# An anagram is a string that contains the exact same characters as another string, 
# but the order of the characters can be different.


    # approach - 1
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sMap, tMap = defaultdict(int), defaultdict(int)
        for i in range(len(s)):
            sMap[s[i]] += 1
            tMap[t[i]] += 1
        return sMap == tMap

    # APPROACH - 2 using counter
    # Counter is a very great in-built function, for counting fequencies.
    # example:-
    #           words = ["apple", "banana", "apple", "orange", "banana", "apple"]
    #           count = Counter(words)
    #           print(count)
    #           output:- Counter({'apple': 3, 'banana': 2, 'orange': 1})

    # APPROACH - 2
    def isAnagram2(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

sol = Solution()
print(sol.isAnagram("anagram", "nagaram"))