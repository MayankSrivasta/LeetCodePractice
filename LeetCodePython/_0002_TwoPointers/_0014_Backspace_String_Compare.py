class Solution:
    # using stack neetcode.io
    def backspaceCompare(self, s: str, t: str) -> bool:
        def convert(s):
            res = []
            for char in s:
                if char == '#':
                    if res:
                        res.pop()
                else:
                    res.append(char)
            return "".join(res)

        return convert(s) == convert(t)

    #   using two pointer approach
    def backspaceCompare1(self, s: str, t: str) -> bool:
        index_s, index_t = len(s) - 1, len(t) - 1
        backspace_s = backspace_t = 0
        
        while True:
            while index_s >= 0 and (backspace_s or s[index_s] == '#'):
                backspace_s += 1 if s[index_s] == '#' else -1
                index_s -= 1

            while index_t >= 0 and (backspace_t or t[index_t] == '#'):
                backspace_t += 1 if t[index_t] == '#' else -1
                index_t -= 1

            if not (index_s >= 0 and index_t >= 0 and s[index_s] == t[index_t]):
                return index_s == index_t == -1
            index_s, index_t = index_s - 1, index_t - 1


    # more simplified approach only in terms of code reading, but approach is same as in above:-
    def backspaceCompare(self, s: str, t: str) -> bool:
        i = len(s) - 1
        j = len(t) - 1
        s_back = 0
        t_back = 0

        while True:
            while i >= 0 and (s_back or s[i] == '#'):
                s_back += 1 if s[i] == '#' else -1
                i -= 1
            
            while j >= 0 and (t_back or t[j] == '#'):
                t_back += 1 if t[j] == '#' else -1
                j -= 1

            if not (i >= 0 and j >= 0 and s[i] == t[j]):
                return i == j == -1
            i -= 1
            j -= 1

print(Solution().backspaceCompare1("ab###c", "ad#c"))