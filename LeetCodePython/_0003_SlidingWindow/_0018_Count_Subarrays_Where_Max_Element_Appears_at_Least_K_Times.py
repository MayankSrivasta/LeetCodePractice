from typing import List
class Solution:
    # sliding window - OPTIMAL
    def countSubarrays(self, nums: List[int], k: int) -> int:
        count = 0  # Frequency of maxNo in the window
        maxNo = max(nums)
        l, res = 0, 0

        for r, num in enumerate(nums):
            # Increment count if the current element is the max element
            if num == maxNo:
                count += 1
            
            # Shrink the window when the count reaches k
            while count == k:
                if nums[l] == maxNo:
                    count -= 1
                l += 1
            
# IMPORTANT:- THE MAIN LOGIC FOR THIS QUESTION IS :-
# CALCUALTE THE RESULT WHEN THE LEFT POINTER STOPS SHIFTING TOWARDS RIGHT.

            # Add valid subarrays ending at r
            res += l
        
        return res

# sliding window
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_n, max_cnt = max(nums), 0
        l = 0
        res = 0

        for r in range(len(nums)):
            if nums[r] == max_n:
                max_cnt += 1
            
            while max_cnt > k or (l <= r and max_cnt == k and nums[l] != max_n):
                if nums[l] == max_n:
                    max_cnt -= 1
                l += 1
            
            if max_cnt == k:
                res += l + 1
        
        return res


print(Solution().countSubarrays([5,5,3,4,1], 2))

# Counting Valid Subarrays:
# At each position r, the number of valid subarrays that end at r is given by l.
# Why l?
# All subarrays starting from indices 0 to l-1 and ending at r are valid.
# Hence, add l to the result:
# res += l
# Why Counting Using Left Pointer (l)?
# When count == k, the subarrays formed from indices [0, l-1] to r become valid.
# Once l moves past the first occurrence where the k count was achieved, the subarrays are no longer valid, and the window is adjusted.

# 🎉 Final Takeaway:
# The sliding window ensures that:
# We count all valid subarrays that contain k occurrences of the maximum element.
# By moving l, we dynamically adjust the window to maintain the condition count == k.