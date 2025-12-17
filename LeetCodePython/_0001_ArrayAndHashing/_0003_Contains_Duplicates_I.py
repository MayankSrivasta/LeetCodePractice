from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

sol = Solution()
print(sol.containsDuplicate([2, 1, 5, 6, 2, 3]))