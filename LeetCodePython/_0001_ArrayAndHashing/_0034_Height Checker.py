from typing import List

class Solution:
# neetcode.io solution
# heights:  [1,1,4,2,1,3]
# expected: [1,1,1,2,3,4]
# follow this approach it is much easier to understand
    def heightChecker(self, heights: List[int]) -> int:
        count = [0] * 101
        for h in heights:
            count[h] += 1

#   creating expected array.
        expected = []
        for h in range(1, 101):
            c = count[h]
            for _ in range(c):
                expected.append(h)

# just compare the values here.
        res = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                res += 1

        return res


# Time Complexity Analysis
# Counting heights takes O(n).
# Reconstructing order and comparing takes O(n).
# Total Complexity → O(n) (faster than O(n log n) sorting approach).
# chatgpt

    def heightChecker(self, heights: List[int]) -> int:
        # Step 1: Count occurrences of each height
        # wanted to map 1 to index 1 and 100 to index 100
        count = [0] * 101  # Since heights range from 1 to 100
        for h in heights:
            count[h] += 1

        # Step 2: Iterate through heights and compare
        mismatch = 0
        index = 0  # Pointer for original array

        for i in range(1, len(heights) + 1):  # Iterate from smallest to largest height
            while count[i] > 0:
                if heights[index] != i:
                    mismatch += 1  # Count the mismatch
                index += 1
                count[i] -= 1  # Reduce frequency
        return mismatch



#  APPROACH - 2
# Counting Sort solution chatgpt
# Time Complexity Analysis
# Sorting takes O(n log n).
# Comparing takes O(n).
# Total Complexity → O(n log n).
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)  # Get the sorted version
        count = 0
        
        # Count mismatched positions
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                count += 1
        
        return count


# Steps:
# Count frequency of each height in heights.
# Rebuild the “expected sorted array” using that frequency table.
# Compare original array with expected → count mismatches.

#   ANOTHER APPROACH FOR THE 1ST ONE - neetcode.io
#   creating a counting sorted array here
    def heightChecker(self, heights: List[int]) -> int:
        count = [0] * 101  # Since heights range from 1 to 100
        for h in heights:
            count[h] += 1


#   In this loop we are creating a COUNTED SORTED ARRAY.
        expected = []
        for h in range(1, 101):
            c = count[h]
            for _ in range(c):
                expected.append(h)

        res = 0
        # Count mismatched positions
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                res += 1

        return res