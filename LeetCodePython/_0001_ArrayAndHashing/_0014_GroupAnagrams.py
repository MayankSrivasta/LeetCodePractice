from collections import defaultdict
from typing import List
from collections import Counter

class Solution:

# without comment->
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for str in strs:
            arr = [0] * 26
            for s in str:
                arr[ord(s) - ord('a')] += 1
            res[tuple(arr)].append(str)
        return list(res.values())

# ====================================================================================================

# Purpose of Using tuple(arr)
# The key idea is that lists are mutable and cannot be used as dictionary keys, whereas tuples are immutable and can be used as keys.

# Breaking It Down:
# arr is a list of size 26, representing the frequency of each letter in a word.
# Since lists cannot be used as dictionary keys, we convert arr into a tuple, making it hashable.
# This tuple acts as a unique identifier for anagrams, ensuring that all words with the same letter frequencies are grouped together.

    # APPROACH - 1
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                # here ord converts the character into ascii substracts the the first character 'a' which
                # reduces its size & moves it into 1, 2, 3, 4, 5 positions in array
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())

# ====================================================================================================

    # APPROACH - 2
    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            res[tuple(sorted(s))].append(s)
        return list(res.values())

# ====================================================================================================

    # APPROACH - 3 using Counter
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)  # Dictionary to store grouped anagrams
        
        for s in strs:
            res[frozenset(Counter(s).items())].append(s)  # Use Counter as a key
            
        return list(res.values())


sol = Solution()
sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"])