# Logic:-
# 1. if the sum of the subarray is odd, then subtract even sum will be odd, 
# because:-
# even + even = even
# odd + even = odd
# odd + odd = even
# even + odd = odd

# YOU HAVE TO GO THROUGH NEETCODE.IO VIDEO 8:55 MINUTES TO UNDERSTAND THE LOGIC BEHIND THIS CODE
# https://neetcode.io/solutions/number-of-sub-arrays-with-odd-sum

from typing import List
# prefix parity counting.
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        cur_sum = odd_cnt = even_cnt = res = 0
        MOD = 10**9 + 7

        for n in arr:
            cur_sum += n
            if cur_sum % 2:
                res = (res + 1 + even_cnt) % MOD
                odd_cnt += 1
            else:
                res = (res + odd_cnt) % MOD
                even_cnt += 1
        return res
#====================================================================================================
    
#   chatgpt
#   below is the code for Counting Even:-
    def EvenNumOfSubarrays(self, arr: List[int]) -> int:
        cur_sum = odd_cnt = even_cnt = res = 0
        MOD = 10**9 + 7

        # Initially, we consider sum 0 as even (empty prefix)
        even_cnt = 1

        for n in arr:
            cur_sum += n
            if cur_sum % 2 == 0:
                res = (res + even_cnt) % MOD
                even_cnt += 1
            else:
                res = (res + odd_cnt) % MOD
                odd_cnt += 1

        return res

# Example usage
arr = [1, 3, 5]
print(Solution.numOfSubarrays(arr))  # Output: 4