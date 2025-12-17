from typing import List
class Solution:

#   two pointer 
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashset = set()
        l = 0
        for r in range(len(nums)):
            # Remove the element that goes out of the k-range window
            if r - l > k:
                hashset.remove(nums[l])
                l += 1
            
            # Check if the current element is already in the hashset
            if nums[r] in hashset:
                return True
            
            # Add the current element to the hashset
            hashset.add(nums[r])
        
        return False

#       hashmap 
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        map = {}
        for i in range(len(nums)):
            if nums[i] in map and i - map[nums[i]] <= k:
                return True
            map[nums[i]] = i
        return False