from collections import Counter
class Solution:
#   sliding window + hashmap
    def checkInclusion2(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)

        if n > m:
            return False

        s1Count = Counter(s1)
        s2Count = Counter(s2[:n - 1])

        for i in range(n - 1, m):
            s2Count[s2[i]] += 1

            k = i - n + 1
            if s1Count == s2Count:
                return True
            
            s2Count[s2[k]] -= 1
        return False