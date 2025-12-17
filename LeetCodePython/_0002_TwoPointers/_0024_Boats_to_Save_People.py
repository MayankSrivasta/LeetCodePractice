from typing import List
class Solution:
    # sorting + two pointer
    # neetcode.io
    # complexity - O(nlogn)
    # space complexity - O(n) or O(n) based upon the sorting algorithm.
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        res, l, r = 0, 0, len(people) - 1
        while l <= r:
            remain = limit - people[r]
            r -= 1
            res += 1
            if l <= r and remain >= people[l]:
                l += 1
        return res
    
    from typing import List

#   chatgpt
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # Sort the people array to apply two-pointer approach
        people.sort()
        l, r = 0, len(people) - 1
        boats = 0
        
        # Two-pointer logic
        while l <= r:
            # Check if lightest and heaviest person can fit in one boat
            if people[l] + people[r] <= limit:
                l += 1  # Pair them together
            
            # Move the right pointer in all cases (heaviest person uses a boat)
            r -= 1
            # Increment boat count
            boats += 1
        
        return boats

    #  O(n)
    #  O(m)
    # Where n is the size of the input array and m is the maximum value in the array.

#   Counting Sort
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        m = max(people)
        count = [0] * (m + 1)
        for p in people:
            count[p] += 1
        
        idx, i = 0, 1
        while idx < len(people):
            while count[i] == 0:
                i += 1
            people[idx] = i
            count[i] -= 1
            idx += 1

        res, l, r = 0, 0, len(people) - 1
        while l <= r:
            remain = limit - people[r]
            r -= 1
            res += 1
            if l <= r and remain >= people[l]:
                l += 1
        return res



#       NOTE To minimize the number of boats:
# Always try to pair the lightest person with the heaviest person.
# If their combined weight exceeds the limit, the heavier person needs a separate boat.
# If they fit, take both in the same boat.