from collections import Counter
class Solution:

# High-Level Idea of This Approach
# This is a two-phase sliding window problem:
# Expand right until window satisfies requirement
# Shrink left to try making it minimal
# This pattern is extremely common in substring queries.

# chatgpt
# Short Code Template (Interview Form)

    def minWindow(s, t):
        if not t or not s: return ""
        
        tcount = Counter(t)
        scount = Counter()
        required = len(tcount)
        formed = 0
        
        l = 0
        res = (inf, None, None)   # (length, left, right)
        
        for r, ch in enumerate(s):
            scount[ch] += 1
            
            if scount[ch] == tcount[ch]:
                formed += 1
            
            while formed == required:
                if r - l + 1 < res[0]:
                    res = (r - l + 1, l, r)
                    
                scount[s[l]] -= 1
                if scount[s[l]] < tcount[s[l]]:
                    formed -= 1
                l += 1
        
        _, L, R = res
        return s[L:R+1] if L is not None else ""

############################################################################################################

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
    
############################################################################################################
# solution submitted on leetcode
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        minLength = float('inf')
        tcount = Counter(t)
        scount = Counter()
        formed = 0
        required = len(tcount)
        str1 = ''
        for r in range(len(s)):

            scount[s[r]] += 1

            if scount[s[r]] == tcount[s[r]]:
               formed += 1
            
            while l <= r and formed == required:
                if r - l + 1 < minLength:
                    minLength = r - l + 1
                    str1 = s[l : r + 1]
                
                scount[s[l]] -= 1
                if s[l] in tcount and scount[s[l]] < tcount[s[l]]:
                    formed -= 1
                
                l += 1

        return str1


print(Solution().minWindow('ADOBEACODEABANC', 'ABACA'))


# 🚨 Similar Problems with Same Approach:
# Find All Anagrams in a String (LeetCode 438)
# Permutation in String (LeetCode 567)
# Longest Substring Without Repeating Characters (LeetCode 3)
# Smallest Window in a String Containing All Characters of Another String
# Substring with Concatenation of All Words (LeetCode 30)