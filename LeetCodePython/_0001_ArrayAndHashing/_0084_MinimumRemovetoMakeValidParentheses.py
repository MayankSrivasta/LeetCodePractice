class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res = []
        cnt = 0  
        # removing extra ) closing parentheses
        for c in s:
            if c == "(":
                res.append(c)
                cnt += 1
            elif c == ")" and cnt > 0:
                res.append(c)
                cnt -= 1
            elif c != ")":      #Append other characters as they are.
                res.append(c)

        filtered = []
        # removing extra ( opening parenthesis
        for c in reversed(res):
            if c == "(" and cnt > 0:
                cnt -= 1
            else:
                filtered.append(c)
        return "".join(reversed(filtered))

print(Solution().minRemoveToMakeValid("lee(t(c)o)de)"))