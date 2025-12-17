class Solution:
    
    # APPROACH - 1
    # Stack - II NEETCODE.IO
    def makeGood(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if stack and abs(ord(s[i]) - ord(stack[-1])) == 32:
                stack.pop()
            else:
                stack.append(s[i])
        return "".join(stack)
    

    # APPROACH - 2
    # TWO POINTER
    def makeGood1(self, s: str) -> str:
        l = 0
        s = list(s)
        for r in range(len(s)):
            if l > 0 and abs(ord(s[r]) - ord(s[l - 1])) == 32:
                l -= 1
            else:
                s[l] = s[r]
                l += 1
        return ''.join(s[:l])
    
print(Solution().makeGood("leEtcode"))    

"""
SOLUTION:-
ASCII values of a and A differ by 32.
You are given a string s.
A string is "great" if no two adjacent characters are the same letter but different cases (like 'a' and 'A').

Rules:
1. If two adjacent characters like 'aA' or 'Bb' appear, they react and both are removed.
2. Keep doing this until no more reactions are possible.
3. Return the final "great" string.

"""