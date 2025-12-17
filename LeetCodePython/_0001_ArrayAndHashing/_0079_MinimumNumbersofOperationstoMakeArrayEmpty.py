from typing import List
from collections import Counter
import math
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = Counter(nums)
        res = 0
        
# for below line u can also use -> for cnt in count.values() because u only need cnt & not the 
# value
        for num, cnt in count.items():
            if cnt == 1:
                return -1
            res += math.ceil(cnt / 3)
        
        return res
# once u get the maths done as below you will automatically understand what maths formula
# should we would be using here.



# cnt	cnt / 3	    math.ceil(cnt / 3)	    Operations Required
# 3	    1.0	            1	                (3) → 1 move
# 4	    1.33	        2	                (3,1) → (2,2) → 2 moves
# 5	    1.67	        2	                (3,2) → 2 moves
# 6	    2.0	            2	                (3,3) → 2 moves
# 7	    2.33	        3	                (3,3,1) → (3,2,2) → 3 moves