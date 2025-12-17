from typing import List
from collections import Counter
from collections import defaultdict

# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

class Solution:
    # 3rd approach
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = defaultdict(int)
        res = 0
        for num in nums:
            res += count[num]
            count[num] += 1
        return res

# chatgpt solutions :-
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans = 0
        freq = {}  # or collections.Counter, or a list of size 101
        for x in nums:
            if x in freq:
                ans += freq[x]
                freq[x] += 1
            else:
                freq[x] = 1
        return ans


    # 1st approach
    def numIdenticalPairs1(self, nums: List[int]) -> int:
        count = Counter(nums)
        res = 0
        for n, c in count.items():
            res += c * (c - 1) // 2
        return res
    
    # 2nd Approach
    def numIdenticalPairs2(self, nums: List[int]) -> int:
        res = 0
        count = {}
        for n in nums:
            if n in count:
                res += count[n]
                count[n] += 1
            else:
                count[n] = 1
        return res
    
sol = Solution()
print(sol.numIdenticalPairs([1,2,3,1,1,3]))