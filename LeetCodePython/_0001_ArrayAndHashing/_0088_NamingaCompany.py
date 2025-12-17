from collections import defaultdict
from typing import List

class Solution:
    # chatgpt solution
    def distinctNames1(self, ideas: List[str]) -> int:
        # Group by first letter and store suffixes in sets
        groups = defaultdict(set)
        
        # ideas = ["coffee", "donuts", "time", "toffee"]
        # grouped = {'c': {"offee", "anteen"}, 'd': {"onuts", "rout"}, 't': {"ime", "offee"}}

        for idea in ideas:
            first_letter, suffix = idea[0], idea[1:]
            groups[first_letter].add(suffix)
        
        valid_names = 0
        letters = list(groups.keys())
        
        # Compare each pair of groups
        for i in range(len(letters)):
            for j in range(i + 1, len(letters)):
                setA, setB = groups[letters[i]], groups[letters[j]]
                
                # Count common suffixes
                common_suffixes = len(setA & setB)
                
                # Count valid combinations
                valid_names += (len(setA) - common_suffixes) * (len(setB) - common_suffixes) * 2
        
        return valid_names


print(Solution().distinctNames2(["coffee","canteen", "donuts", "drout", "time", "toffee"]))
