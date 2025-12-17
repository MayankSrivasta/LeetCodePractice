from typing import List

class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        shift = 0
        str_arr = list(s)
        for i in range(len(str_arr) - 1, -1, -1):
            shift = (shift + shifts[i]) % 26
            shifted_char = chr((ord(str_arr[i]) - ord('a') + shift) % 26 + ord('a'))
            str_arr[i] = shifted_char

        return ''.join(str_arr)

from typing import List

class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        n = len(s)
        total_shift = 0
        result = [''] * n

        for i in range(n - 1, -1, -1):
            total_shift = (total_shift + shifts[i]) % 26
            result[i] = chr((ord(s[i]) - ord('a') + total_shift) % 26 + ord('a'))

        return ''.join(result)


#         creating reverse prefix sum
#     Given ->       3        5       9
#                  3+5+9    5 + 9     9
#     shifts =      17       14       9 now shifting each characters by these numbers


