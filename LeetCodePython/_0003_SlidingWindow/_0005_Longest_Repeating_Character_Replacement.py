from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        
        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res
    

    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)  # Using defaultdict to handle frequency
        l = 0  # Left pointer
        maxFreq = 0  # Max frequency of any character in the window
        res = 0  # To store the max length of valid window

        for r in range(len(s)):
            count[s[r]] += 1  # Increment frequency of s[r]
            maxFreq = max(maxFreq, count[s[r]])

            # Check if the number of replacements exceeds k
            if (r - l + 1) - maxFreq > k:
                count[s[l]] -= 1  # Remove leftmost element from the window
                l += 1  # Shrink the window

            # Update result with the longest valid window length
            res = max(res, r - l + 1)

        return res


