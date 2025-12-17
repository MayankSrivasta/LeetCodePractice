class Solution:

#   sliding window
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        l = 0
        res = 0
        for r in range(len(s)):
            maxCost -= abs(ord(s[r]) - ord(t[r]))
            if maxCost < 0:
                maxCost += abs(ord(s[l]) - ord(t[l]))
                l += 1
            res = max(res, r - l + 1)
        return res
    
# NOTE:- TRY TO FIND THE REASON WHY return len(s) - l WORKS TO GET THE MAX LENGTH. ALSO WHEN WE HAVE res = max(res, r - l + 1)
# 🎯 Conclusion
# ✅ len(s) - l works because l only moves when necessary.
# ✅ The final window at the end is the longest valid one.
# ⚠️ If the max-length substring occurs earlier, explicit tracking (maxLen) is safer.