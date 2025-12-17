from typing import List
from collections import defaultdict, Counter
class Solution:
    # Neetcode solution
    # its not given properly in the question that we need to find the max frequency of each character in words2
    # and then check if the each word in words1 has all the characters in words2 with the max frequency
    # w1 is the subset of w2
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        count_2 = defaultdict(int)
        for w in words2:
            count_w = Counter(w)
            for c, cnt in count_w.items():
                count_2[c] = max(count_2[c], cnt)

        res = []
        for w in words1:
            count_w = Counter(w)
            flag = True
            for c, cnt in count_2.items():
                if count_w[c] < cnt:
                    flag = False
                    break
            if flag:
                res.append(w)
        return res


# chatgpt solution
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
                
        # Step 1: Create max frequency requirement from words2
        max_freq = defaultdict(int)
        for word in words2:
            word_count = Counter(word)
            for c in word_count:
                max_freq[c] = max(max_freq[c], word_count[c])

        # Step 2: Filter words1 that meet the max_freq requirement
        res = []
        for word in words1:
            word_count = Counter(word)
            if all(word_count[c] >= max_freq[c] for c in max_freq):
                res.append(word)
        return res


print(Solution().wordSubsets(["amazon","apple","facebook","google","leetcode"], ["e","o"]))
# Output: ["facebook","google","leetcode"]



# The Real Role of max()
# words2 = ["lo", "cool"]

# Counter("lo") → {l:1, o:1}

# Counter("cool") → {c:1, o:2, l:1}

# You want to build a final requirement that ensures:

# c appears at least 1 time

# o appears at least 2 times (not 1)

# l appears at least 1 time