from typing import List
class Solution:
    # approach - 1
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        num_set = set(nums)  # Store existing numbers in a set
        n = len(nums)
        missing_numbers = []
        for i in range(1, n + 1):
            if i not in num_set:
                missing_numbers.append(i)
        return missing_numbers

#====================================================================================================

    # the same above line can be written like this also in a single line
    # approach - 2
    def findDisappearedNumbers2(self, nums: List[int]) -> List[int]:
        num_set = set(nums)  # Store existing numbers in a set
        n = len(nums)
        return [i for i in range(1, n + 1) if i not in num_set]