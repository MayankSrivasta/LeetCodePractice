class MyQueue:

#   Using Two Stacks - CHATGPT

# How it works:
# in_stack is for pushing new elements.
# out_stack is for popping or peeking elements.
# Whenever out_stack is empty and you need to pop/peek, you move all elements from in_stack 
# to out_stack (reversing the order, making it FIFO).

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        self.peek()  # Move elements if needed
        return self.out_stack.pop()

    def peek(self) -> int:  # its purpose is to push elements from in_stack to out_stack
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[-1]

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack



# USING Single Stack + Recursion -> CHATGPT
    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if not self.stack:
            return None
        top = self.stack.pop()
        if not self.stack:
            # This is the bottom element (front of queue)
            return top
        else:
            result = self.pop()
            self.stack.append(top)
            return result

    def peek(self) -> int:
        val = self.pop()
        self.stack.append(val)
        return val

    def empty(self) -> bool:
        return not self.stack
