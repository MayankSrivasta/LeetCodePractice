from typing import List
class Solution:
    
    
    # logci was each word in words, for each word(single) (its all characters should be present in allowed)
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        res = len(words)
        for w in words:
            for c in w:
                if c not in allowed:
                    res -= 1
                    break
        return res

#====================================================================================================

    # approach - 2 chatgpt
def countConsistentStrings(allowed: str, words: List[str]) -> int:
    allowed_set = set(allowed)
    res = 0
    for w in words:
        if all(c in allowed_set for c in w):
            res += 1
    return res

#====================================================================================================

# approach-3 chatgpt
def countConsistentStrings(allowed: str, words: List[str]) -> int:
    allowed_set = set(allowed)
    res = 0
    for w in words:
        good = True
        for c in w:
            if c not in allowed_set:
                good = False
                break
        if good:
            res += 1
    return res