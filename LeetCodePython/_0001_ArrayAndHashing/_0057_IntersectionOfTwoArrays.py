from typing import List
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = set(nums1)
        res = []
        for n in nums2:
            if n in seen:
                res.append(n)
                seen.remove(n)
        return res

sol = Solution()
print(sol.intersection([4, 9, 5], [9,1,4,2,9,8,4]))

# its telling us to return -> array of elements -> but actually its confusing us,
# -> we just have to return the common elements between the two given arrays/list



class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))
