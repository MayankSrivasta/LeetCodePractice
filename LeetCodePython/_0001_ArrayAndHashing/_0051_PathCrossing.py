class Solution:
    def isPathCrossing(self, path: str) -> bool:
        # Map directions to coordinate changes
        # consider dir_map just like hashmap
        dir_map = {
            'N': (0, 1),
            'S': (0, -1),
            'E': (1, 0),
            'W': (-1, 0)
        }
        visit = set()  # To track visited positions
        x, y = 0, 0
        visit.add((x, y))  # Add the starting point

        for v in path:
            dx, dy = dir_map[v]
            x += dx
            y += dy

            # Check if new position has been visited
            if (x, y) in visit:
                return True
            visit.add((x, y))

        return False