class Solution:
    # hashset neetcode.io solution
    def hasAllCodes(self, s: str, k: int) -> bool:
        if len(s) < 2 ** k:
            return False
        
        codeSet = set()
        for i in range(len(s) - k + 1):
            codeSet.add(s[i:i + k])
        
        return len(codeSet) == 2 ** k