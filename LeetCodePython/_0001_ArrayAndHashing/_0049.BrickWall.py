from typing import List
from collections import defaultdict
class Solution:

# APPROACH - 1
    def leastBricks(self, wall: List[List[int]]) -> int:
        countGap = { 0 : 0 }    # { Position : Gap count }

        for r in wall:
            total = 0   # Position
            for b in r[:-1]:
                total += b
                countGap[total] = 1 + countGap.get(total, 0)

        return len(wall) - max(countGap.values())    # Total number of rows - Max gap


# APPROACH - 2
    def leastBricks(self, wall: List[List[int]]) -> int:
            
            countGap = defaultdict(int)  # Initialize with default integer values

            for row in wall:
                position = 0
                # Sum up to each brick except the last, marking gap positions
                for brick in row[:-1]:
                    position += brick
                    countGap[position] += 1

            # Calculate minimum bricks crossed by subtracting the max gap count from total rows
            maxGaps = max(countGap.values(), default=0)
            return len(wall) - maxGaps

    def leastBricks2(self, wall: List[List[int]]) -> int:
        hashmap = {}
        for w in wall:
             gap = 0
             for c in w[: -1]:
                gap += c
                hashmap[gap] = 1 + hashmap.get(gap, 0)
        
        return len(wall) - max(hashmap.values(), default=0)

        



sol = Solution()
print(sol.leastBricks2([[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]))