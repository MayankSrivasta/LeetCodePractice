class Solution:

# is it ok since ab is coming twice in the partitions -> 
# ✅ Correct partitions: ["ab", "ac", "ab", "a"]

# ChatGPT said:
# Yes, it's okay! The goal of Optimal Partition of String is to minimize the number of 
# partitions while ensuring that each character appears only once per partition—not necessarily 
# to make all partitions unique.

# Even though "ab" appears twice, each partition individually maintains the rule that no character 
# is repeated within it.

# So, ✅ ["ab", "ac", "ab", "a"] is a valid answer. However, depending on how you break the partitions,
#  there could be other valid answers too! The key is to minimize the number of partitions while 
# maintaining uniqueness in each one.

    def partitionString(self, s: str) -> int:
        curSet = set()
        res = 1
        for c in s:
            if c in curSet:
                res += 1
                curSet.clear()
            curSet.add(c)
        return res
    
    # abacaba