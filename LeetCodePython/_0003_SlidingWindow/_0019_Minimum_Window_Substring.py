from collections import Counter
class Solution:
    # chatgpt
    # Input: s = "ADOBECODEBANC", t = "ABC"
    def minWindow2(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        tCount = Counter(t)
        windowCount = Counter()

        i, minLength = 0, float('inf')
        required, formed = len(tCount), 0
        strRes = ""

        for j, ch in enumerate(s):
            # Add character to window
            windowCount[ch] += 1

            # If current character matches frequency needed in t
            if ch in tCount and windowCount[ch] == tCount[ch]:
                formed += 1

            # Try to shrink the window when all characters are matched
            while i <= j and formed == required:
                # Update result if smaller window found
                if j - i + 1 < minLength:
                    minLength = j - i + 1
                    strRes = s[i:j + 1]    
                
                # Remove character from the left of the window
                windowCount[s[i]] -= 1
                if s[i] in tCount and windowCount[s[i]] < tCount[s[i]]:
                    formed -= 1

                # Move left pointer to shrink the window
                i += 1
        
        return strRes
    
print(Solution().minWindow('ADOBEACODEABANC', 'ABACA'))


# 🚨 Similar Problems with Same Approach:
# Find All Anagrams in a String (LeetCode 438)
# Permutation in String (LeetCode 567)
# Longest Substring Without Repeating Characters (LeetCode 3)
# Smallest Window in a String Containing All Characters of Another String
# Substring with Concatenation of All Words (LeetCode 30)