from typing import List

class Solution:
    # this question approach is easy but is not straight forward but observation based
    # so you have to observe it & accordingly proceed onto with it.
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        res = 0
        for i in range(len(tickets)):
            # check video again in case u r not able to understand again or properly
            if i <= k:
                res += min(tickets[i], tickets[k])
            else:
                # case -> 2, 3, 10 -> 2 + 3 + 2
                res += min(tickets[i], tickets[k] - 1)
        return res

sol = Solution()
print(sol.timeRequiredToBuy([2,3,2], 2))

"""
Breaking It Down
Case 1: i ≤ k
These are people before or at k in the queue.
They will always get served as long as person k is still buying.
So, they can be served at most tickets[k] times.
Contribution = min(tickets[i], tickets[k])

Case 2: i > k
These are people after k in the queue.
Once person k buys their last ticket, we stop — so these people get at most tickets[k] - 1 turns.
Contribution = min(tickets[i], tickets[k] - 1)
"""