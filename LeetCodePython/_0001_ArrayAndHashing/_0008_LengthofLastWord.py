class Solution:
    # approach - 1
# ⏱️ Time Complexity: O(n)
# 💾 Space Complexity: O(1)
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        i = len(s) - 1
        while s[i] == ' ':
            i -= 1
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1
        return length
    


#   approach - 2
# ⏱️ Time Complexity: O(n)
# 💾 Space Complexity: O(n) (because of split list)
    class Solution:
        def lengthOfLastWord(self, s: str) -> int:
            return len(s.strip().split()[-1])
        
"""
s.strip() → remove extra spaces at both ends
.split() → split the string into words based on spaces
[-1] → get the last word
len(...) → get the length of that last word
"""