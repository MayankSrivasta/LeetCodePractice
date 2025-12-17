class Solution:
    # using stack
    def minSwaps(self, s: str) -> int:
        stack = []
        for c in s:
            if c == '[':
                stack.append(c)
            elif stack:
                stack.pop()
        return (len(stack) + 1) // 2
    
    # greedy approach
    # https://www.youtube.com/watch?v=kYTQgaNDc9o
    def minSwaps2(self, s: str) -> int:
        close = maxClose = 0

        for c in s:
            if c == '[':
                close -= 1
            else:
                close += 1
            maxClose = max(maxClose, close)
        
        return (maxClose + 1) // 2
    
print(Solution().minSwaps2([']][[']))