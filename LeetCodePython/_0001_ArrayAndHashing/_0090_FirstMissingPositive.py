from typing import List
class Solution:
    # chatgpt
    # video for understanding
    # https://www.youtube.com/watch?time_continue=82&v=SEn4fyMZ22M&embeds_referring_euri=https%3A%2F%2Fleetcode.com%2F

    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Step 1: Swap elements to their correct positions
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        
        # Step 2: Check for the first missing positive
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        # Step 3: If all positions are correct, return n + 1
        return n + 1
