def explain_subarray_sum():
    """
    Visual explanation of how prefix sum works for finding subarrays that sum to k
    """
    print("""
    Example: nums = [1, -1, 1, 1, 1, 1, 1], k = 3
    
    Prefix Sums visualization:
    Index:    0   1   2   3   4   5   6
    Array:    1  -1   1   1   1   1   1
    PreSum:   1   0   1   2   3   4   5
    
    prefixSums dictionary evolution:
    Initially: {0: 1}
    
    Step 1: curSum = 1
    {0: 1, 1: 1}
    [-----------------]
     1
    
    Step 2: curSum = 0
    {0: 2, 1: 1}
    [-----------------]
     1  -1
    
    Step 3: curSum = 1
    {0: 2, 1: 2}
    [-----------------]
     1  -1   1
    
    Step 4: curSum = 2
    {0: 2, 1: 2, 2: 1}
    [-----------------]
     1  -1   1   1
    
    Step 5: curSum = 3  (Found k!)
    {0: 2, 1: 2, 2: 1, 3: 1}
    [-----------------]
     1  -1   1   1   1
                [-----] Subarray sum = 3
    
    Step 6: curSum = 4
    {0: 2, 1: 2, 2: 1, 3: 1, 4: 1}
    [-----------------]
     1  -1   1   1   1   1
                [-----] Subarray sum = 3
                    [-----] Subarray sum = 3
    
    Step 7: curSum = 5
    {0: 2, 1: 2, 2: 1, 3: 1, 4: 1, 5: 1}
    [-----------------]
     1  -1   1   1   1   1   1
                [-----] Subarray sum = 3
                    [-----] Subarray sum = 3
                        [-----] Subarray sum = 3
    
    When we find curSum - k in prefixSums:
    * It means we found a subarray that sums to k
    * The count in prefixSums tells us how many such subarrays end at current position
    
    Formula: Current subarray sum = Current prefix sum - Previous prefix sum
    If we want sum = k, then:
    k = Current prefix sum - Previous prefix sum
    Previous prefix sum = Current prefix sum - k
    
    Total subarrays that sum to 3: 5
    """)

if __name__ == "__main__":
    explain_subarray_sum()