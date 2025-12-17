from typing import List
from collections import defaultdict
from collections import Counter

class Solution:
      # approach - 1
    def makeEqual(self, words: List[str]) -> bool:
        char_cnt = Counter(words)
        
        for c in char_cnt:
            if char_cnt[c] % len(words) :
                return False
        return True
    
    # approach - 2
    def makeEqual(self, words: List[str]) -> bool:
        charCount = Counter("".join(words))  # Count all characters in words
        
        return all(count % len(words) == 0 for count in charCount.values())

sol = Solution()
print(sol.makeEqual(["abc","aabc","bc"]))