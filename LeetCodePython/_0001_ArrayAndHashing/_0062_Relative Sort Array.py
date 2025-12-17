from typing import List
from collections import defaultdict
from collections import Counter
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:

        count = defaultdict(int)
        end = []
        for n in arr1:
            if n not in arr2:
                end.append(n)
            count[n] += 1
        end.sort()
        
        res = []
        for n in arr2:
            for i in range(count[n]):
                res.append(n)
        return res + end
    
#   chatgpt 
# Approach 2: Using sorted() with a Lambda Function
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        order = {num: i for i, num in enumerate(arr2)}  # Map values in arr2 to their index
        
        return sorted(arr1, key=lambda x: (order.get(x, len(arr2) + x), x))

# approach - 3
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = Counter(arr1)  # Count occurrences in arr1
        
        # First, add elements from arr2 in the correct order
        result = []
        for num in arr2:
            result.extend([num] * count[num])  # Add num count[num] times
            del count[num]  # Remove from count
        
        # Add the remaining elements (not in arr2), sorted in ascending order
        for num in sorted(count.keys()):
            result.extend([num] * count[num])
        
        return result
