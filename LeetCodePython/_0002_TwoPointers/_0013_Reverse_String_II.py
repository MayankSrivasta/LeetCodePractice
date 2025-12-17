class Solution:

    # not in neetcode.io, solution from chatgpt

#     Handle Edge Cases:
#     If the remaining characters are fewer than k, reverse them all.
#     If the remaining characters are between k and 2k, reverse only the first k.
    def reverseStr(self, s: str, k: int) -> str:
        # Convert the string to a list for in-place modification
        s = list(s)
        n = len(s)
        
        # Iterate through the string with a step of 2k
        for i in range(0, n, 2 * k):
            # Reverse the first k characters within the range [i, i + k]
            s[i:i + k] = reversed(s[i:i + k])
        
        # Join the list back to form the final string
        return ''.join(s)


# same code but without comments
    def reverseStr(self, s: str, k: int) -> str:
        n = len(s)
        s = list(s)
        for i in range(0, n, 2 * k):
            s[i : i + k] = reversed(s[i : i + k])
        return "".join(s)


print(Solution().reverseStr("abcdefgh", 3))
# o/p   -> cbadefhg



⚡️ Key Difference Between [::-1] and reversed():
[::-1] creates a new list in reverse order.

reversed() returns a reverse iterator that can be used to modify the list in place.

✅ Both approaches are valid, but reversed() is considered more memory efficient since it doesn’t create a new list if used with nums[:].