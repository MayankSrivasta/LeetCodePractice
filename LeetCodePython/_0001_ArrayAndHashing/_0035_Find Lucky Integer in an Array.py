from collections import Counter
from collections import defaultdict

# COUNTER
def findLucky(arr):
    freq = Counter(arr)
    lucky = -1
    for num, count in freq.items():
        if num == count:
            lucky = max(lucky, num)
    return lucky


# Approach 2: Dictionary (manual frequency map)
def findLucky(arr):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    
    lucky = -1
    for num, count in freq.items():
        if num == count:
            lucky = max(lucky, num)
    
    return lucky

# approach 3 using defaultdict
def findLucky(arr):
    freq = defaultdict(int)   # default value for each key is 0
    
    # build frequency map
    for num in arr:
        freq[num] += 1
    
    lucky = -1
    # check for lucky integers
    for num, count in freq.items():
        if num == count:
            lucky = max(lucky, num)
    
    return lucky