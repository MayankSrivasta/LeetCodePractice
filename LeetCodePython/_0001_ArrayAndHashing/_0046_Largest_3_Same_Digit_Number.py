class Solution:

    def largestGoodInteger(self, num: str) -> str:
        res = ""
        for i in range(len(num) - 2):
            if num[i] == num[i + 1] == num[i + 2]:
                res = max(res, num[i:i + 3])
        return res



# Example usage:
sol = Solution()
print(sol.largestGoodInteger("6777133339"))  # Output: "777"
print(sol.largestGoodInteger("2300019"))     # Output: "000"
print(sol.largestGoodInteger("42352338"))    # Output: ""