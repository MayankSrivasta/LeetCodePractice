# Explanation: Subarrays Divisible by K

## Problem Example
Input: `nums = [4, 5, 0, -2, -3, 1]`, `k = 5`

## Step-by-Step Solution

### Initialization
- `prefix_sum = 0`
- `res = 0` (count of valid subarrays)
- `prefix_count = {0: 1}` (for prefix sums divisible by k)

### Iterations

#### 1. n = 4
- prefix_sum = 4
- remain = 4
- prefix_count = {0: 1, 4: 1}
- res = 0

#### 2. n = 5
- prefix_sum = 9
- remain = 4
- prefix_count = {0: 1, 4: 2}
- Subarrays: [5]
- res = 1

#### 3. n = 0
- prefix_sum = 9
- remain = 4
- prefix_count = {0: 1, 4: 3}
- Subarrays: [5, 0], [0]
- res = 3

#### 4. n = -2
- prefix_sum = 7
- remain = 2
- prefix_count = {0: 1, 4: 3, 2: 1}
- res = 3

#### 5. n = -3
- prefix_sum = 4
- remain = 4
- prefix_count = {0: 1, 4: 4, 2: 1}
- Subarrays: [5, 0, -2, -3], [0, -2, -3], [-2, -3]
- res = 6

#### 6. n = 1
- prefix_sum = 5
- remain = 0
- prefix_count = {0: 2, 4: 4, 2: 1}
- Subarrays: [4, 5, 0, -2, -3, 1], [5, 0, -2, -3, 1]
- res = 8

## All Valid Subarrays
1. [5]
2. [5, 0]
3. [0]
4. [5, 0, -2, -3]
5. [0, -2, -3]
6. [-2, -3]
7. [4, 5, 0, -2, -3, 1]
8. [5, 0, -2, -3, 1]

## Final Result
Total subarrays divisible by k = 5: **8**
