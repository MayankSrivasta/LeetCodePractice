from typing import List
class Solution:


# BRUTE FORCE APPROACH:-
# O(n^2 * m^2)
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        
        # Compare each word with all other words
        for i, word in enumerate(words):
            for j, otherWord in enumerate(words):
                # i & j is getting checked so that it doesn't checks itself
                if i != j and word in otherWord:
                    res.append(word)
                    break  # Avoid duplicates if word is found multiple times
        return res

# ====================================================================================================
    
#   from Leetcode solution:-
    def stringMatching2(self, words: List[str]) -> List[str]:
        res = []
        for i, w in enumerate(words):
            for j, x in enumerate(words):
                if i != j and w in x:
                    res.append(w)
                    break
        return res    

# ====================================================================================================

# from Neetcode.io solution:-
# https://neetcode.io/solutions/string-matching-in-an-array
# else you can use other STRING MATCHING ALGO:-
# 1. KMP - difficult algo.
# 2. Rabin Karp - most optimal- difficult algo.
# 3. Z-Algorithm
# 4. Trie