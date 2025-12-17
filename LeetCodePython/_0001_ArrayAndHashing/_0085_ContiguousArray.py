from typing import List
class Solution:
    # hashmap approach
    def findMaxLength(self, nums: List[int]) -> int:
        zero = one = res = 0
        diff_index = {}

        for i, n in enumerate(nums):
            if n == 0:
                zero += 1
            else:
                one += 1

            if one - zero not in diff_index:
                diff_index[one - zero] = i

            if one == zero:
                res = one + zero
            else:
                idx = diff_index[one - zero]
                res = max(res, i - idx)

        return res
    
    # https://www.youtube.com/watch?v=Xkl4EknqW8Y&t=617s    watch video from 2 minutes
    def findMaxLength(self, nums: List[int]) -> int:

        # { 0 : -1}

        seen_at = {0: -1}
        ans = count = 0
        for i, num in enumerate (nums) :
            count += 1 if num else -1

            if count in seen_at:
                ans = max(ans, i - seen_at[count])
            else:
                seen_at[count] = i
        return ans