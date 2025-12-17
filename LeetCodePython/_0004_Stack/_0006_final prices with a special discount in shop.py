
class Solution:

# Quick Intuition on Stack Approach:
# Use a stack to remember the indices of prices.
# If you find a price lower than or equal to the one on top of the stack → apply the 
# discount immediately by popping the index and updating prices[idx] -= prices[i].

    def finalPrices(prices):
        stack = []
        for i in range(len(prices)):
            while stack and prices[stack[-1]] >= prices[i]:
                idx = stack.pop()
                prices[idx] -= prices[i]
            stack.append(i)
        return prices