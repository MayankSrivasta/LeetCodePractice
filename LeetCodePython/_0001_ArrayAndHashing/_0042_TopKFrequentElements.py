from typing import List
from collections import defaultdict
from collections import Counter
class Solution:
    def topKFrequent1(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)  # Automatically initializes missing keys to 0

        # it creates array like -> freq -> [[], [], [], [], [], [], []]
        freq = [[] for _ in range(len(nums) + 1)]

#       the above line can be written as below
        # freq = []
        # for _ in range(len(nums) + 1):
        #     freq.append([])

        # Step 1: Count frequency of each element
        for num in nums:
            count[num] += 1  # No need for .get() method

        # Step 2: Bucket Sort - Place numbers in corresponding frequency index
        for num, cnt in count.items():
            freq[cnt].append(num)

        # Step 3: Extract top K frequent elements
        res = []
        for i in range(len(freq) - 1, 0, -1):  # Start from highest frequency
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res  # Stop early when we have K elements

#   written in much clearer form:
# check FREQ COUNTER diagram for better understanding
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = [[] for i in range(len(nums) + 1)]

        count = Counter(nums)            
        
        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res


nums = [1, 1, 1, 2, 2, 3]
k = 2
sol = Solution()
print(sol.topKFrequent(nums, k))  # Output: [1, 2]