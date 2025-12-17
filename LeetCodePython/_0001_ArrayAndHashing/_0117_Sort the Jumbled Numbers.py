from typing import List
class Solution:
    # neetcode.io solution
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        pairs = []

        for i, n in enumerate(nums):
            n = str(n)
            mapped_n = 0
            for c in n:
                mapped_n *= 10
                mapped_n += mapping[int(c)]
            pairs.append((mapped_n, i))

        pairs.sort()
        return [nums[p[1]] for p in pairs]
    

    
    # chatgpt solution
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def mapped_value(num):
            return int("".join(str(mapping[int(d)]) for d in str(num)))

        # Pair each number with its mapped value, then sort based on mapped value
        return sorted(nums, key=mapped_value)
