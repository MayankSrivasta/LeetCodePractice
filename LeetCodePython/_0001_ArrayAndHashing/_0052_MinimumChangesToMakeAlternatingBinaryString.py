class Solution:
    def minOperations(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            if i % 2: # odd index        Step 1: Checking "0101..." Pattern
                count += 1 if s[i] == '0' else 0
            else: # even index           Step 2: Checking "1010..." Pattern
                count += 1 if s[i] == '1' else 0
        return min(count, len(s) - count)
    
sol = Solution()
print(sol.minOperations("0100"))


# chatgpt
def minOperations(s: str) -> int:
    mismatch1 = 0
    for i, ch in enumerate(s):
        expected = '0' if i % 2 == 0 else '1'  # pattern "0101..."
        if ch != expected:
            mismatch1 += 1
    
    n = len(s)
    mismatch2 = n - mismatch1
    return min(mismatch1, mismatch2)
