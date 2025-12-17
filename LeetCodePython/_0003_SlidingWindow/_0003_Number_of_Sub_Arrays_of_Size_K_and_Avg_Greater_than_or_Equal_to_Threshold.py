from typing import List
class Solution:
#   sliding window neetcode.io  ==>  properly understand how prefix sum is also done for this type of question
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        windowSum = sum(arr[: k - 1])
        n = len(arr)
        for i in range(n - k + 1):
            windowSum += arr[i + k - 1]
            if (windowSum / k) >= threshold:
                res += 1
            windowSum -= arr[i]
        return res


#   prefix sum
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        prefix_sum = [0] * (len(arr) + 1)
        for i in range(len(arr)):
            prefix_sum[i + 1] += prefix_sum[i] + arr[i]

        res = l = 0
        for r in range(k - 1, len(arr)):
            sum_ = prefix_sum[r + 1] - prefix_sum[l]
            if sum_ / k >= threshold:
                res += 1
            l += 1
        
        return res