from typing import List
class Solution:

    def maxAscendingSum(self, nums: List[int]) -> int:
        res = nums[0]
        curSum = nums[0]
        for i in range(1, len(nums)):
            if nums[i - 1] >= nums[i]:
                curSum = 0
            curSum += nums[i]
            res = max(curSum, res)
        return res


#   neetcode.io
    def maxAscendingSum(self, nums: List[int]) -> int:
        curSum = results = nums[0]

        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                curSum = 0
            curSum += nums[i]
            results = max(curSum, results)

        return results

# 🎯 Related Problems
# Longest Increasing Subarray - LeetCode #674
# Maximum Subarray Sum - LeetCode #53
# Longest Continuous Increasing Subsequence - LeetCode #674