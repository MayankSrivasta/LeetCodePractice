from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        L = 0
        for R in range(len(nums)):
            l = len(window)
            if l > k:
                window.remove(nums[L])
                L += 1
            if nums[R] in window:
                return True
            window.add(nums[R])
        return False

    # approach - 2
    # here K is window size
    def containsNearbyDuplicate2(self, nums: List[int], k: int) -> bool:
        hashset = set()
        L = 0
        for R in range(len(nums)):
            if R - L > k:
                hashset.remove(nums[L])
                L += 1
            if nums[R] in hashset:
                return True
            hashset.add(nums[R])
        return False    

sol = Solution()
print(sol.containsNearbyDuplicate([1,2,3,4,1], k = 3))