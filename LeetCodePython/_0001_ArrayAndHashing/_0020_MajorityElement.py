from collections import defaultdict
from typing import List
from collections import Counter

class Solution:
    # approach - 1
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        res = maxCount = 0

        for num in nums:
            count[num] += 1
            if maxCount < count[num]:
                res = num
                maxCount = count[num]
        return res
    
    # APPRACH - 2 solved within single line
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)  # Get frequency of each number
        return max(count, key=count.get)  # Return element with max frequency

    
    # approach - 3  Boyer-Moore Voting Algorithm - BEST APPROACH
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = 0
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if candidate == num else -1)
        return candidate
    

#   approach - 4
    def majorityElement(self, nums: List[int]) -> int:
        map = defaultdict(int)
        result = maxCount = 0
        for i in range(len(nums)):
            map[nums[i]] += 1
            if maxCount < map[nums[i]]:
                maxCount = map[nums[i]]
                result = nums[i]

        return result

#      approach - 5
#      Boyer-Moore Voting Algorithm - O(N)
#      https://www.geeksforgeeks.org/boyer-moore-majority-voting-algorithm/

    def majorityElement2(self, nums: List[int]) -> int:
        candidate = None
        count = 0

        # Step 1: Find the candidate
        for num in nums:
            if count == 0:
                candidate = num  # Set new candidate
            count += (1 if num == candidate else -1)

        # Step 2 (Optional): Verify candidate
        return candidate  # Assumption: Majority element always exists
