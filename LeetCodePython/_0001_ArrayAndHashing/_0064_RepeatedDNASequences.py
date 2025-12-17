from typing import List
from collections import defaultdict

class Solution:

    # hashset
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen, res = set(), set()

        for l in range(len(s) - 9):
            cur = s[l: l + 10]
            if cur in seen:
                res.add(cur)
            seen.add(cur)
        return list(res)

    # hashmap
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []

        mp = defaultdict(int)
        res = []
        for l in range(len(s) - 9):
            cur = s[l: l + 10]
            mp[cur] += 1
            if mp[cur] == 2:
                res.append(cur)

        return res

    # Rabin-Karp Algorithm (Double Hashing)
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        if n < 10:
            return []

        cnt = defaultdict(int)
        res = []
        base1, base2 = 31, 37
        hash1 = hash2 = 0
        power1, power2 = 1, 1
        MOD1, MOD2 = 685683731, 768258391

        for i in range(9):
            power1 *= base1
            power2 *= base2
            power1 %= MOD1
            power2 %= MOD2

        for i in range(n):
            hash1 = (hash1 * base1 + ord(s[i])) % MOD1
            hash2 = (hash2 * base2 + ord(s[i])) % MOD2

            if i >= 9:
                key = (hash1 << 31) | hash2
                cnt[key] += 1
                if cnt[key] == 2:
                    res.append(s[i - 9 : i + 1])

                hash1 = (hash1 - power1 * ord(s[i - 9]) % MOD1 + MOD1) % MOD1
                hash2 = (hash2 - power2 * ord(s[i - 9]) % MOD2 + MOD2)

        return res