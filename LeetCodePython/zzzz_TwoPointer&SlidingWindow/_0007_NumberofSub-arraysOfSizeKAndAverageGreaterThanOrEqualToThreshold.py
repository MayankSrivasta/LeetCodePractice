from typing import List
class Solution:
    # approach - 1
    def numOfSubarrays(arr, k, threshold):
        target_sum = k * threshold
        current_sum = sum(arr[:k])

        if current_sum >= target_sum:
            count = 1
        else:
            count = 0 
    
        for i in range(k, len(arr)):
            current_sum += arr[i] - arr[i - k]
            if current_sum >= target_sum:
                count += 1
        return count

# approach - 2
    def numOfSubarrays(arr, k, threshold):
        curr_sum = 0  # To store the sum of the current window
        count_k = 0  # To track the window size
        count_res = 0  # To store the result count
        length = len(arr)
        
        for i in range(length):
            curr_sum += arr[i]
            count_k += 1
            
            # Check if the window size is at least k
            if count_k >= k:
                avg = curr_sum / k
                if avg >= threshold:
                    count_res += 1
                    
                # Shift the window by subtracting the first element of the current window
                curr_sum -= arr[i + 1 - k]
        
        return count_res

    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        curr_sum = 0  # To store the sum of the current window
        count_k = 0  # To track the window size
        count_res = 0  # To store the result count
        length = len(arr)
        
        for i in range(length):
            curr_sum += arr[i]
            count_k += 1
            
            # Check if the window size is at least k
            if count_k >= k:
                avg = curr_sum / k
                if avg >= threshold:
                    count_res += 1
                    
                # Shift the window by subtracting the first element of the current window
                curr_sum -= arr[i + 1 - k]
        return count_res
    
#   sliding window - 1 from neetcode.io
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        curSum = sum(arr[:k - 1])

        for L in range(len(arr) - k + 1):
            curSum += arr[L + k - 1]
            if (curSum / k) >= threshold:
                res += 1
            curSum -= arr[L]
        return res