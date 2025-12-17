class Solution:
    # approach - 1 using set
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


    # approach - 2
    # using hashmap
    # s = "abcabcbb"
    def with_hash_map(s: str) -> int:
        hm = {}  # Dictionary to store the last occurrence of each character
        i = -1  # Correctly set to -1 since no characters are processed initially
        ans = 0  # To keep track of the longest substring length
        n = len(s)  # Length of the input string

        for j, ch in enumerate(s):
            if ch in hm:
                i = max(hm[ch], i)  # Update i to the last occurrence of ch or keep it unchanged

            hm[ch] = j  # Update the last occurrence of the character
            ans = max(ans, j - i)  # Update the maximum length (no need for '+ 1')

        return ans