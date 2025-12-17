# Problem: Make Sum Divisible by P
# Given an array of integers nums and an integer p, remove the minimum number of elements from 
# nums such that the sum of the remaining elements is divisible by p. Return the minimum number 
# of elements you need to remove, or -1 if it's impossible.


# https://leetcode.com/problems/make-sum-divisible-by-p/editorial/
# READ THOUGH THE LEETCODE EDITOR, FOR PROPER EXPLANATION FOR "target".

def minSubarray(nums, p):
    # Step 1: Calculate the total sum and remainder
    total_sum = sum(nums)
    remainder = total_sum % p
    if remainder == 0:
        return 0

    # Step 2: Initialize variables
    prefix_sum = 0
    min_length = len(nums)
    prefix_map = {0: -1}

    # Step 3: Iterate through the array
    for i, num in enumerate(nums):
        prefix_sum = (prefix_sum + num) % p
        target = (prefix_sum - remainder + p) % p
        if target in prefix_map:
            min_length = min(min_length, i - prefix_map[target])
        prefix_map[prefix_sum] = i

    # Step 4: Return the result
    return min_length if min_length < len(nums) else -1

# Explanation:
# This function solves the problem of finding the smallest subarray in the list `nums` that, 
# when removed, makes the sum of the remaining elements divisible by `p`. If no such subarray 
# exists, it returns `-1`.

# Step-by-step explanation:
# 1. Calculate the total sum of the array and its remainder when divided by `p`.
#    If the remainder is 0, the total sum is already divisible by `p`, so return 0.
# 2. Use a prefix sum approach to track cumulative sums modulo `p` as we iterate through the array.
# 3. Use a dictionary (`prefix_map`) to store the indices of prefix sums modulo `p` for efficient lookups.
# 4. For each element, calculate the target value needed to form a subarray whose removal makes the sum divisible by `p`.
# 5. If the target exists in `prefix_map`, calculate the subarray length and update the minimum length if it's smaller.
# 6. Return the minimum length if a valid subarray is found; otherwise, return -1.

# Example usage
nums = [3, 1, 4, 2]
p = 6
print(minSubarray(nums, p))  # Output: 1