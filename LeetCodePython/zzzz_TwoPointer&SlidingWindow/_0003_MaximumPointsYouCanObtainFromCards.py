from typing import List

class Solution:
    # APPROACH - 1
    def max_score(card_points, k):
        # Initial left sum (taking the first k cards from the left)
        lsum = sum(card_points[:k])
        total_sum = lsum
    
        # Initialize right sum as 0
        rsum = 0
        j = len(card_points) - 1
    
        # Iterate backwards over the first k elements
        # for l in range(start, stop, step):
        for i in range(k - 1, -1, -1):
            lsum -= card_points[i]  # Remove the element from the left sum
            rsum += card_points[j]  # Add the element from the right to the right sum
            j -= 1
        
            # Update the total sum (max of current sum or lsum + rsum)
            total_sum = max(total_sum, lsum + rsum)
    
        return total_sum

    # APPROACH - 2
    def max_score(cards, k):
        n = len(cards)
        total_sum = sum(cards)

        if n == k:
            return total_sum

        # Initialize the window sum for the first (n - k) elements
        window_sum = sum(cards[:n - k])

        # Initialize max score by subtracting the initial window from the total sum
        max_score = total_sum - window_sum

        # Two-pointer sliding window approach: Slide the window through the array
        for i in range(n - k, n):
            window_sum += cards[i]                # Add current element to the window
            window_sum -= cards[i - (n - k)]      # Remove the leftmost element of the window
            max_score = max(max_score, total_sum - window_sum)

        return max_score