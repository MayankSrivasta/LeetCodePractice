from collections import defaultdict
from typing import List

# not in Neetcode.io list
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        unique_count = len(set(nums))
        n = len(nums)
        left = 0
        right = 0
        freq = defaultdict(int)
        complete_subarrays = 0

        while left < n:
            while right < n and len(freq) < unique_count:
                freq[nums[right]] += 1
                right += 1

            if len(freq) < unique_count:
                break

            complete_subarrays += n - right + 1

            freq[nums[left]] -= 1
            if freq[nums[left]] == 0:
                del freq[nums[left]]
            left += 1

        return complete_subarrays

print(Solution().countCompleteSubarrays([3,1,1,2,2]))