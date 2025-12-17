from typing import List

class Solution:
    # BACKTRACKING APPROACH
    # 1. only add open parrenthesis if open < n
    # 2. only add a closing parenthesis if closed < open
    # 3. valid IIF open == closed == n
    # the backtracking steps are followed & given in Leecode Python Sheet.
        

    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def backtrack(current, open_count, close_count):
            if len(current) == 2 * n:
                result.append(current)
                return
            
            if open_count < n:
                backtrack(current + "(", open_count + 1, close_count)
            
            if close_count < open_count:
                backtrack(current + ")", open_count, close_count + 1)

        backtrack("", 0, 0)
        return result

# iterative approach

    def generateParenthesis2(self, n: int) -> List[str]:
        stack = [("", 0, 0)]
        result = []

        while stack:
            current, open_count, close_count = stack.pop()

            if len(current) == 2 * n:
                result.append(current)
                continue

            if open_count < n:
                stack.append((current + "(", open_count + 1, close_count))

            if close_count < open_count:
                stack.append((current + ")", open_count, close_count + 1))

        return result


# dynamic programming chatgpt
    def generateParenthesis(self, n):
        res = [[] for _ in range(n+1)]
        res[0] = [""]
        
        for k in range(n + 1):
            for i in range(k):
                for left in res[i]:
                    for right in res[k-i-1]:
                        res[k].append("(" + left + ")" + right)
        
        return res[-1]

# Example usage:
sol = Solution()
print(sol.generateParenthesis2(3))