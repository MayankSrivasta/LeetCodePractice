from typing import List
from collections import defaultdict
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        total_pairs = (n * (n - 1)) // 2
        good_pair = 0
        count = defaultdict(int)
        for i, v in enumerate(nums):
            key = v - i
            good_pair += count[key]     # how many times we've seen this key (good_pairs) before
            count[key] += 1
        return total_pairs - good_pair


# Intuition
# Let’s first understand the condition:
# A pair (i, j) is bad if:
# j - i ≠ nums[j] - nums[i]

# Let’s simplify this condition:
#                                    j - i ≠ nums[j] - nums[i]
#                                    nums[j] - j ≠ nums[i] - i
# So now the condition becomes:

                                    # A pair (i, j) is bad if nums[j] - j ≠ nums[i] - i

# For all possible (i, j) where i < j, count how many times nums[i] - i ≠ nums[j] - j.
# 💡 Optimized Approach
                    # Count the number of good pairs, where:
                    # nums[i] - i == nums[j] - j     # how many times we've seen this key before