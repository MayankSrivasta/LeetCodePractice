from typing import List
from collections import Counter
class Solution:
    # create hashmap/counter for each word & then accordingly compare them & then create a list of common 
    # characters, check video or python sheet for the image
    def commonChars(self, words: List[str]) -> List[str]:

        cnt = Counter(words[0])
        
        for w in words[1:]:
            currCnt = Counter(w)
            for c in cnt:
                cnt[c] = min(cnt[c], currCnt[c])

        result = []
        for c, freq in cnt.items():
            result.extend([c] * freq)

        return result
    
# chatgpt
class Solution:
    def commonChars(self, words):
        # Start with character count of first word
        common = Counter(words[0])
        
        # Intersect with each word's Counter
        # below line is not very much clear understanding
        for w in words[1:]:
            common &= Counter(w)   # keeps min count for each char
        
        # Expand into result list
        result = []
        for c, freq in common.items():
            result.extend([c] * freq)
        
        return result