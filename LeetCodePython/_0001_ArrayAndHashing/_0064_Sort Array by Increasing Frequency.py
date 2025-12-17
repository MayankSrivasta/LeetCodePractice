from collections import Counter
from typing import List
class Solution:
#   approach - 1
#  
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)  # Count frequency of each number
        return sorted(nums, key=lambda x: (freq[x], -x))  # Sort by frequency, then by value (descending)


#   approach - 2
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        
        # Create buckets where index = frequency
        # it creates array like -> freq -> [[], [], [], [], [], [], []]
#       it is created as a list inside list 
        buckets = [[] for _ in range(len(nums) + 1)]
        
        for num, count in freq.items():
            buckets[count].append(num)
        
        result = []
        for count, bucket in enumerate(buckets):
            for num in sorted(bucket, reverse=True):  # Sort descending within the same frequency
                result.extend([num] * count)
        
        return result
    
# Use Counter to count occurrences.
# Create buckets → Each bucket holds numbers that appear count times.
# Sort numbers within each bucket in descending order (since we need to prioritize larger numbers when frequencies are equal).
# Flatten the buckets into the final array.