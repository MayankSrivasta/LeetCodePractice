package _0004_Stack;

import java.util.Stack;

public class _0002_MinStack {

	private Stack<Integer> stack;
	private Stack<Integer> minStack;

	public _0002_MinStack() {
		stack = new Stack<>();
		minStack = new Stack<>();
	}

	public void push(int val) {
		stack.push(val);
		val = Math.min(val, minStack.isEmpty() ? val : minStack.peek());
		minStack.push(val);
	}

	public void pop() {
		stack.pop();
		minStack.pop();
	}

	public int top() {
		return stack.peek();
	}

	public int getMin() {
		return minStack.peek();
	}
}
