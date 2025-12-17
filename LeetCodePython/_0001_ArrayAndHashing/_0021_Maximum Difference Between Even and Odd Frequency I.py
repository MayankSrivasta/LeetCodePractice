from collections import defaultdict
from collections import Counter

class Solution:
    def maxDifference(self, s: str) -> int:

        freq = Counter(s)
        max_odd = 0
        # Set min_even to something large, bigger than any possible freq
        # Since s length ≤ 100, you can use len(s) + 1 or just float('inf')
        min_even = float('inf')
        
        for v in freq.values():
             # odd
            if v % 2 == 1:
                if v > max_odd:
                    max_odd = v
            # even
            else:    
                if v > 0 and v < min_even:
                    min_even = v
        
        # Because the problem guarantees at least one odd and one even
        # We don't need to handle the case where one of them is missing
        return max_odd - min_even
    
    # above ones cleaner approach
    def maxDifference(self, s: str) -> int:
        freq = Counter(s)
        max_odd = float('-inf')
        min_even = float('inf')
        
        for v in freq.values():
            if v % 2 == 1:
                max_odd = max(max_odd, v)
            else:
                min_even = min(min_even, v)
        
        return max_odd - min_even


    
    # chatgpt
    def maxDifference(s: str) -> int:
        # Step 1: Count frequencies of each character
        freq = Counter(s)
        
        # Step 2: Separate even and odd frequencies
        even_freqs = [f for f in freq.values() if f % 2 == 0]
        odd_freqs = [f for f in freq.values() if f % 2 != 0]
        
        # Step 3: If either list is empty, return -1
        if not even_freqs or not odd_freqs:
            return -1
        
        # Step 4: Compute maximum difference
        max_diff = max(even_freqs) - min(odd_freqs)
        return max_diff