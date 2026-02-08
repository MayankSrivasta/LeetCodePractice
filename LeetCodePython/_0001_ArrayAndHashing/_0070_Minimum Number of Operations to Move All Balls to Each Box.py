from typing import List
class Solution:
    # neetcode video solution
    def minOperations(self, boxes: str) -> List[int]:
        res = [0] * len(boxes)
        balls, moves = 0, 0

        for i in range(len(boxes)):
            res[i] = balls + moves
            moves = moves + balls
            balls += int(boxes[i])
        
        balls, moves = 0, 0
        for i in reversed (range (len(boxes) )):
            res[i] += balls + moves
            moves = moves + balls
            balls += int(boxes [i])
        return res

#====================================================================================================

#   Cherry Coding [IIT-G] youtube channel...
    def minOperations2(self, boxes: str) -> List[int]:
        n = len(boxes)
        res = [0] * n
        ahead = 0
        behind = 0

        # First pass: calculate total cost to bring all balls to index 0
        for i in range(n):
            if boxes[i] == '1':
                ahead += 1
                res[0] += i

        # Update ahead and behind if box[0] has a ball
        if boxes[0] == '1':
            ahead -= 1
            behind += 1

        # Second pass: use previous result to build the rest
        for i in range(1, n):
            res[i] = res[i - 1] - ahead + behind
            if boxes[i] == '1':
                ahead -= 1
                behind += 1

        return res

print(Solution().minOperations('001011'))

#====================================================================================================

# 🔍 How It Works:
# ahead tracks number of balls to the right of the current index.
# behind tracks number of balls to the left.
# We initialize res[0] with the total moves required to bring all balls to index 0.
# For each subsequent index, we incrementally update the result using:
# res[i] = res[i-1] - ahead + behind

#====================================================================================================

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        res = [0] * n
        ahead = 0
        behind = 0
        for i in range(n):
            if boxes[i] == '1':
                res[i] += i
                ahead += 1
        
        if boxes[0] == '1':
            behind += 1
            ahead -= 1
        
        for i in range(1, n):
            res[i] = res[i - 1] - ahead + behind
            ahead -= 1
            behind += 1
        
        return res