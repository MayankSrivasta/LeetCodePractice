package _0004_Stack;

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class _0004_GenerateParentheses {

	public List<String> generateParenthesis(int n) {
		List<String> res = new ArrayList<>();
		Stack<Character> stack = new Stack<>();
		backtrack(n, 0, 0, stack, res);
		return res;
	}

	private void backtrack(int n, int openN, int closedN, Stack<Character> stack, List<String> res) {
		if (openN == closedN && openN == n) {
			StringBuilder sb = new StringBuilder();
			for (char c : stack) {
				sb.append(c);
			}
			res.add(sb.toString());
			return;
		}

		if (openN < n) {
			stack.push('(');
			backtrack(n, openN + 1, closedN, stack, res);
			stack.pop();
		}
		if (closedN < openN) {
			stack.push(')');
			backtrack(n, openN, closedN + 1, stack, res);
			stack.pop();
		}
	}

	public static void main(String[] args) {
		_0004_GenerateParentheses solution = new _0004_GenerateParentheses();
		System.out.println(solution.generateParenthesis(3));
	}

	public List<String> generateParenthesis2(int n) {
		List<String> list = new ArrayList();
		Stack<Character> stack = new Stack();
		backtrack(n, 0, 0, list, stack);
		return list;

	}

	public static void backtrack(int n, int open, int close, List<String> list, Stack<Character> stack) {

		if (open == close && open == n) {
			StringBuilder sb = new StringBuilder();
			for (char ch : stack)
				sb.append(ch);
			list.add(sb.toString());
		}

		if (open < n) {
			stack.add('(');
			backtrack(n, open + 1, close, list, stack);
			stack.pop();
		}

		if (close < open) {
			stack.add(')');
			backtrack(n, open, close + 1, list, stack);
			stack.pop();
		}

	}

}
