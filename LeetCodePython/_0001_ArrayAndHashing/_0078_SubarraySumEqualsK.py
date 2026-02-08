from typing import List
from collections import defaultdict

class Solution:

# NEETCODE.IO VIDEO -> 8:15 MINUTES

# check your notes copy for some better understanding, refer - [1, 2, 3, 4, 5] example


# The hashmap initially contains {0:1}.
# Since 0 exists, we know that a subarray starting from index 0 to index 1 directly sums to k, so we count this as a valid subarray.
# Why Initialize {0:1}?
# This ensures that when the prefix_sum itself equals k, we count it as a valid subarray.
# Without {0:1}, we would miss counting cases where the first few elements sum to k directly.

    # brute force:-
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        for i in range(len(nums)):
            sum = 0
            for j in range(i, len(nums)):
                sum += nums[j]
                if sum == k:
                    res += 1
        return res
    
#===========================================================================================================   

    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curSum = 0
        prefixSums = { 0 : 1 }
        for n in nums:
            curSum += n
            diff = curSum - k
            # NOTE:-
            # If prefix_sum - k exists in the hashmap, that means there exists a previous prefix sum where a subarray ending at the current index sums to k.
            # Increase total_subarrays count by how many times prefix_sum - k has been seen.

            #   -> if previous prefix exists, which means that if you keep on calculating the prefix sum by going forward, & when u substract the k value from the prefix sum, if it gives u the existing prefix sum value then the added values in the prefix sum is equivalent to k.
            # which means (previous prefix sum +  k = current prefix sum value)
            res += prefixSums.get(diff, 0)
            prefixSums[curSum] = 1 + prefixSums.get(curSum, 0)

        return res
    
#===========================================================================================================    

    # chatgpt
    def subarraySum1(self, nums: List[int], k: int) -> int:
        res = 0
        curSum = 0
        prefixSums = defaultdict(int)
        prefixSums[0] = 1  # To handle cases where subarray starts from index 0
        
        for n in nums:
            curSum += n
            res += prefixSums[curSum - k]  # No need to use .get(), defaultdict initializes missing keys to 0
            prefixSums[curSum] += 1  # Increment the count of prefix sum

        return res

# Solution().subarraySum1([1, -1, 1, 1, 1, 1, 1], 3)
# print(Solution().subarraySum1([1, 2, 10, 11, 12], 3))
print(Solution().subarraySum1([1, 2, 3, 4, 5], 3))