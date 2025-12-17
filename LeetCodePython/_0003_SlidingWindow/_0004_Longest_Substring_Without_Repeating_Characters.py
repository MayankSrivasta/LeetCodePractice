class Solution:

#   sliding window        
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res
    


    # sliding window + hashmap
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        l = 0
        res = 0
        
        for r in range(len(s)):
            if s[r] in mp:
                l = max(mp[s[r]] + 1, l)
            mp[s[r]] = r
            res = max(res, r - l + 1)
        return res
    
#     ⚠️ Why max() is Used:
# hm[s[j]] + 1: Moves i to the position after the duplicate.

# i: Ensures that i does not move backward.

# 👉 If the current value of i is already ahead of hm[s[j]] + 1, we don't move i back to avoid 
# shrinking the window unnecessarily.

    # chatgpt
    def lengthOfLongestSubstring(self, s: str) -> int:

        hm = {}  # Dictionary to store the last occurrence of each character
        i = -1  # Correctly set to -1 since no characters are processed initially
        ans = 0  # To keep track of the longest substring length
        n = len(s)  # Length of the input string

        for j, ch in enumerate(s):
            if ch in hm:
                i = max(hm[ch], i)
            hm[ch] = j
            ans = max(ans, j - i)
        return ans
        