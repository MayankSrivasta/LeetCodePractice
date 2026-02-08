class MinStack:
    # using two stack
    # chatgpt - complexity - O(1)

# APPROACH - 1
    # neetcode.io using only 1-stack, complexity - O(n)
    # using single stack uses tuple based insertion into stack, check below example
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        current_min = val if not self.stack else min(val, self.stack[-1][1])
        self.stack.append((val, current_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]

################################################################################################################################################################

# push(5)
# push(3)
# push(7)
# push(2)

# [
#     (5, 5),   # push 5 → min so far = 5
#     (3, 3),   # push 3 → min so far = 3
#     (7, 3),   # push 7 → min so far = still 3
#     (2, 2)    # push 2 → new min = 2
# ]

################################################################################################################################################################


# stack keeps all elements.
# min_stack keeps current minimums.
# Only push into min_stack if the new element is smaller or equal to current min.
# When popping, if the popped element was the minimum, pop from min_stack too.

# Maintain two stacks:
# Main stack → holds all values
# Min stack → holds the min at each level only when useful

#   APPROACH - 2

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # Push to min_stack only if smaller or equal
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]