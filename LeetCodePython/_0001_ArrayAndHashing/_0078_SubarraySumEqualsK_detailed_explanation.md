# Subarray Sum Equals K - Detailed Explanation

This document provides a comprehensive explanation of the "Subarray Sum Equals K" problem and its solutions.

## Problem Statement

Given an array of integers `nums` and an integer `k`, find the total number of subarrays whose sum equals `k`.

A subarray is a contiguous non-empty sequence of elements within an array.

## 1. Brute Force Approach

```python
def subarraySum(self, nums: List[int], k: int) -> int:
    res = 0
    for i in range(len(nums)):
        sum = 0
        for j in range(i, len(nums)):
            sum += nums[j]
            if sum == k:
                res += 1
    return res
```

### How it works:

- Uses two nested loops to check every possible subarray
- For each starting position `i`, it tries all ending positions `j` from `i` to the end
- Calculates the sum of each subarray and checks if it equals `k`
- Time complexity: O(n²) - inefficient for large arrays

## 2. Optimized Solution (Prefix Sum + HashMap)

```python
def subarraySum(self, nums: List[int], k: int) -> int:
    res = 0
    curSum = 0
    prefixSums = { 0 : 1 }
    for n in nums:
        curSum += n
        diff = curSum - k
        res += prefixSums.get(diff, 0)
        prefixSums[curSum] = 1 + prefixSums.get(curSum, 0)
    return res
```

### Key Concepts:

1. **Prefix Sum**: A running sum of elements as we iterate through the array
2. **HashMap**: Stores the frequency of each prefix sum encountered
3. **The Critical Insight**: If at the current position our prefix sum is `curSum`, and we've previously seen a prefix sum of `curSum - k`, then there must be a subarray with sum `k` between those positions

### Why Initialize `prefixSums = {0: 1}`?

This initialization handles the case where a subarray starting from index 0 has a sum of exactly `k`. Without this, we would miss counting subarrays that start from the beginning of the array.

### Step-by-Step Explanation:

1. Initialize:
   - `res = 0`: Counter for valid subarrays
   - `curSum = 0`: Running sum
   - `prefixSums = {0: 1}`: HashMap with initial value

2. For each element `n` in the array:
   - Add it to the running sum: `curSum += n`
   - Calculate the difference: `diff = curSum - k`
   - Check if `diff` exists in our HashMap:
     - If it does, it means there's a previous prefix sum where the subarray between that point and the current position sums to `k`
     - Add the frequency of that prefix sum to our result: `res += prefixSums.get(diff, 0)`
   - Update the HashMap with the current prefix sum: `prefixSums[curSum] = 1 + prefixSums.get(curSum, 0)`

### The Mathematical Logic:

If at position `j` we have a prefix sum `curSum`, and at some previous position `i` we had a prefix sum of `curSum - k`, then the subarray from `i+1` to `j` must sum to exactly `k`.

This is because:
- Prefix sum at position `j` = sum of elements from index 0 to j
- Prefix sum at position `i` = sum of elements from index 0 to i
- Therefore, sum from `i+1` to `j` = (prefix sum at j) - (prefix sum at i) = `curSum - (curSum - k) = k`

## Example Walkthrough:

For array `[1, 2, 3]` with `k = 3`:

1. Initialize: `res = 0`, `curSum = 0`, `prefixSums = {0: 1}`
2. Process `1`:
   - `curSum = 1`
   - `diff = 1 - 3 = -2`
   - `prefixSums[-2]` doesn't exist, so `res` remains `0`
   - Update `prefixSums = {0: 1, 1: 1}`
3. Process `2`:
   - `curSum = 3`
   - `diff = 3 - 3 = 0`
   - `prefixSums[0] = 1`, so `res = 1`
   - Update `prefixSums = {0: 1, 1: 1, 3: 1}`
4. Process `3`:
   - `curSum = 6`
   - `diff = 6 - 3 = 3`
   - `prefixSums[3] = 1`, so `res = 2`
   - Update `prefixSums = {0: 1, 1: 1, 3: 1, 6: 1}`
5. Return `res = 2` (the subarrays are `[1, 2]` and `[3]`)

## Another Example:

For array `[1, -1, 1, 1, 1, 1]` with `k = 3`:

1. Initialize: `res = 0`, `curSum = 0`, `prefixSums = {0: 1}`
2. Process `1`:
   - `curSum = 1`
   - `diff = 1 - 3 = -2`
   - `prefixSums[-2]` doesn't exist, so `res` remains `0`
   - Update `prefixSums = {0: 1, 1: 1}`
3. Process `-1`:
   - `curSum = 0`
   - `diff = 0 - 3 = -3`
   - `prefixSums[-3]` doesn't exist, so `res` remains `0`
   - Update `prefixSums = {0: 2, 1: 1}`
4. Process `1`:
   - `curSum = 1`
   - `diff = 1 - 3 = -2`
   - `prefixSums[-2]` doesn't exist, so `res` remains `0`
   - Update `prefixSums = {0: 2, 1: 2}`
5. Process `1`:
   - `curSum = 2`
   - `diff = 2 - 3 = -1`
   - `prefixSums[-1]` doesn't exist, so `res` remains `0`
   - Update `prefixSums = {0: 2, 1: 2, 2: 1}`
6. Process `1`:
   - `curSum = 3`
   - `diff = 3 - 3 = 0`
   - `prefixSums[0] = 2`, so `res = 2`
   - Update `prefixSums = {0: 2, 1: 2, 2: 1, 3: 1}`
7. Process `1`:
   - `curSum = 4`
   - `diff = 4 - 3 = 1`
   - `prefixSums[1] = 2`, so `res = 4`
   - Update `prefixSums = {0: 2, 1: 2, 2: 1, 3: 1, 4: 1}`
8. Return `res = 4` (the subarrays are `[1, 1, 1]`, `[1, 1, 1]`, `[3]`, and `[1, -1, 1, 1, 1]`)

## Time and Space Complexity:

- Time Complexity: O(n) - we only need to iterate through the array once
- Space Complexity: O(n) - in the worst case, we might need to store n different prefix sums

This approach is significantly more efficient than the brute force method, especially for large arrays.

## Alternative Implementation with defaultdict:

```python
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
```

This implementation uses Python's `defaultdict` to simplify the code by automatically initializing missing keys to 0, eliminating the need for the `.get()` method.
