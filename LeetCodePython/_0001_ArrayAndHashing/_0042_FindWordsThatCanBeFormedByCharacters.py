from typing import List
from collections import Counter
from collections import defaultdict

class Solution:
    def countcharacters(self, words: List[str], chars: str) -> int:
        count = Counter (chars)
        res = 0
        for w in words:
            cur_word = defaultdict(int)
            good = True
            for c in w:
                cur_word[c] += 1
                if c not in count or cur_word[c] > count[c]:
                    good = False
                    break
            if good:
                res += len(w)
        return res
    

# BETTER APPROACH reducing unnecessary codes
    def countCharacters2(self, words: List[str], chars: str) -> int:
        count = Counter(chars)
        res = 0
        for w in words:
            wCount = Counter(w)
            good = True
            for c in w:
                if wCount[c] > count[c]:
                    good = False
                    break
            res += len(w) if good else 0
        return res


    def countCharacters3(words: List[str], chars: str) -> int:
        count = Counter(chars)
        res = 0
        for w in words:
            wCount = Counter(w)
            good = True
            for c in w:
                if wCount[c] > count[c]:   # no need for .get(c, 0)
                    good = False
                    break
            res += len(w) if good else 0
        return res


    
sol = Solution()
print(sol.countcharacters(["cat","bt","hat","tree"], "atach"))