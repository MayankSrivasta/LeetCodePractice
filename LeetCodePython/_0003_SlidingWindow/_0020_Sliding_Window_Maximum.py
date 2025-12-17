from typing import List
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque()  # index
        l = r = 0

        while r < len(nums):
            # if the new coming value is greater than the existing value in the dqueue, keeps on 
            # remove it
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

#   Check if the Left Pointer l Exceeds the Front of the Queue:
# If l > q[0], it means the element at q[0] has moved out of the window, so we remove it using popleft().
            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1

        return output
    
print(Solution().maxSlidingWindow([1, 1, 1, 1, 1, 4, 5], 6))