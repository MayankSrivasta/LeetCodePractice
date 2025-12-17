from typing import List
# sweep line algorithm, neetcode.io solution
# READ 'DIFFERENCE ARRAY' FROM LEETCODE EDITORIALS.
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix_diff = [0] * (len(s) + 1)

        for left, right, d in shifts:
            val = 1 if d == 1 else -1
            prefix_diff[left] += val
            prefix_diff[right + 1] -= val

        diff = 0
        res = [ord(c) - ord("a") for c in s]

        for i in range(len(s)):
            diff += prefix_diff[i]
            res[i] = (diff + res[i] + 26) % 26

        s = [chr(ord("a") + n) for n in res]
        return "".join(s)

# chatgpt
#       previous 2 question are inter-related to each other, u have to understand previous 2 question 
#   to understand this one, it is completely based on the trick given in 'Range Addition' Question
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        diff = [0] * (n + 1)  # one extra for easier prefix sum calculation

        # 1. Apply each shift as a difference update
        for start, end, direction in shifts:
            delta = 1 if direction == 1 else -1
            diff[start] += delta
            diff[end + 1] -= delta

        # 2. Build prefix sum to get net shift at each index
        for i in range(1, n):
            diff[i] += diff[i - 1]

        # 3. Shift characters using net shift
        res = []
        for i in range(n):
            net_shift = diff[i] % 26  # wrap around alphabet
            old_char = s[i]
            new_char = chr((ord(old_char) - ord('a') + net_shift) % 26 + ord('a'))
            res.append(new_char)

        return ''.join(res)


print(Solution().shiftingLetters("abc", [[0,1,0],[1,2,1],[0,2,1]]))