class Solution:

#  O(N+N^2) - using One Stack
# https://www.youtube.com/watch?v=qB0zZpBJlh8 - 6 mins
    def decodeString(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                # getting substring
                substr = ""
                while stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop()

                # getting count
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                #                 
                stack.append(int(k) * substr)

        return "".join(stack)
    

#   Using Two Stack:-
    def decodeString(self, s: str) -> str:
        string_stack = []
        count_stack = []
        cur = ""
        k = 0

        for c in s:
            if c.isdigit():
                k = k * 10 + int(c)
            elif c == "[":
                string_stack.append(cur)
                count_stack.append(k)
                cur = ""
                k = 0
            elif c == "]":
                temp = cur
                cur = string_stack.pop()
                count = count_stack.pop()
                cur += temp * count
            else:
                cur += c

        return cur