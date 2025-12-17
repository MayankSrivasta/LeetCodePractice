from typing import List
from collections import defaultdict
class Solution:
    # neetcode.io
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        res = 0
        prefix_count = defaultdict(int)
        prefix_count[0] = 1

        for n in nums:
            prefix_sum += n
            remain = prefix_sum % k
            if remain < 0:
                remain += k
            # Check if the current prefix sum's remainder has been seen before
            # If so, it means there are subarrays that sum to a multiple of k
            # between the previous occurrence and the current index
            # Add the count of such occurrences to the result
            # Increment the count of this remainder in the prefix_count dictionary
            # to account for future subarrays that may also be divisible by k
            
            res += prefix_count[remain]
            prefix_count[remain] += 1
        return res
    

# GitHub Copilot
# To solve the problem of finding subarrays divisible by k, we use the prefix sum and remainder approach. Here's how the algorithm works step-by-step for the input nums = [4, 5, 0, -2, -3, 1] and k = 5:

# Step-by-Step Execution:
# Initialization:

# prefix_sum = 0
# res = 0 (to store the count of valid subarrays)
# prefix_count = {0: 1} (to handle cases where the prefix sum itself is divisible by k)
# Iterate through the array: For each element in nums, calculate the cumulative prefix_sum, compute the remainder (remain), and update the result (res) and the prefix_count.

# Iteration Details:

# Step 1: Process n = 4
# prefix_sum = 0 + 4 = 4
# remain = 4 % 5 = 4
# prefix_count = {0: 1, 4: 1} (add remain to prefix_count)
# No subarrays found yet (res = 0).

# Step 2: Process n = 5
# prefix_sum = 4 + 5 = 9
# remain = 9 % 5 = 4
# prefix_count = {0: 1, 4: 2} (increment count for remain = 4)
# Subarrays ending here: [5] (increment res by prefix_count[4] = 1).
# res = 1.

# Step 3: Process n = 0
# prefix_sum = 9 + 0 = 9
# remain = 9 % 5 = 4
# prefix_count = {0: 1, 4: 3} (increment count for remain = 4)
# Subarrays ending here: [5, 0], [0] (increment res by prefix_count[4] = 2).
# res = 3.

# Step 4: Process n = -2
# prefix_sum = 9 + (-2) = 7
# remain = 7 % 5 = 2 (adjusted to positive remainder)
# prefix_count = {0: 1, 4: 3, 2: 1} (add remain = 2)
# No subarrays found (res = 3).

# Step 5: Process n = -3
# prefix_sum = 7 + (-3) = 4
# remain = 4 % 5 = 4
# prefix_count = {0: 1, 4: 4, 2: 1} (increment count for remain = 4)
# Subarrays ending here: [5, 0, -2, -3], [0, -2, -3], [-2, -3] (increment res by prefix_count[4] = 3).
# res = 6.

# Step 6: Process n = 1
# prefix_sum = 4 + 1 = 5
# remain = 5 % 5 = 0
# prefix_count = {0: 2, 4: 4, 2: 1} (increment count for remain = 0)
# Subarrays ending here: [4, 5, 0, -2, -3, 1], [5, 0, -2, -3, 1] (increment res by prefix_count[0] = 2).
# res = 8.

# Final Result:
# The total number of subarrays divisible by k = 5 is 8.