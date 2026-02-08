class Solution:
    # Prefix and Suffix
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        cnt = 0

        prefixN = []
        for c in customers:
            prefixN.append(cnt)
            if c == 'N':
                cnt += 1
        prefixN.append(cnt)
        
        suffixY = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffixY[i] = suffixY[i + 1]
            if customers[i] == 'Y':
                suffixY[i] += 1
        
        res = n
        minPenalty = n
        for i in range(n + 1):
            penalty = prefixN[i] + suffixY[i]
            if penalty < minPenalty:
                minPenalty = penalty
                res = i
        
        return res
#====================================================================================================
    
    # Iteration - One Pass
    def bestClosingTime2(self, customers: str) -> int:
        res = minPenalty = 0
        penalty = 0

        for i, c in enumerate(customers):
            penalty += 1 if c == 'Y' else -1

            if penalty > minPenalty:
                minPenalty = penalty
                res = i + 1

        return res