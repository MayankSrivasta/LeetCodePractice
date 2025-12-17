from typing import List
class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        t = 0       # current time
        total = 0

        for arrival, order in customers:
            if t > arrival:
                total += t - arrival
            else:
                t = arrival
            total += order
            t += order
        return total / len(customers)
    

    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        t = 0
        total = 0

        for arrival, order in customers:
            total += max(t - arrival, 0)
            t = max(t, arrival)
            total += order
            t += order
        return total / len(customers)