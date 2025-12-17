from collections import Counter

class Solution:
#   just writing this without comments
#   sliding window + hashmap
    def findAnagrams(self, s: str, p: str):
        res = []
        n, m = len(s), len(p)

        if n < m:
            return res
        
        pCount = Counter(p)
        sCount = Counter(s[:m-1])

        for i in range(m - 1, n):
            sCount[s[i]] += 1
            k = i - m + 1
            if sCount == pCount:
                res.append(k)
            
            sCount[s[k]] -= 1
            if sCount[s[k]] == 0:
                del sCount[s[k]]
        return res

    # from Chatgpt
    def findAnagrams1(self, s: str, p: str):
        res = []
        n, m = len(s), len(p)
        if n < m:
            return res  # If s is shorter than p, return empty list
        
        # Frequency count of p and the initial window in s
        p_count = Counter(p)
        s_count = Counter(s[:m-1])  # First m-1 characters in s
        
        for i in range(m-1, n):
            # Include the new character in the window
            s_count[s[i]] += 1
            
            # Compare both frequency maps
            if s_count == p_count:
                res.append(i - m + 1)  # Store starting index
            
            # Remove the character going out of the window
            s_count[s[i - m + 1]] -= 1
            if s_count[s[i - m + 1]] == 0:
                del s_count[s[i - m + 1]]  # Remove keys with 0 frequency
        
        return res
    
Solution().findAnagrams("cbaebabacd", "abc")