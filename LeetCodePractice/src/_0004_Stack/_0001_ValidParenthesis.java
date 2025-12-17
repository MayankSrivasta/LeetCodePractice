package _0004_Stack;

import java.util.HashMap;
import java.util.Map;
import java.util.Stack;

public class _0001_ValidParenthesis {

//	APPROACH - 1
	public boolean isValid1(String s) {
		Stack<Character> stack = new Stack<>();

		for (char c : s.toCharArray()) {
			if (c == '(' || c == '{' || c == '[') {
				stack.push(c);
			} else if (c == ')' && !stack.isEmpty() && stack.peek() == '(') {
				stack.pop();
			} else if (c == '}' && !stack.isEmpty() && stack.peek() == '{') {
				stack.pop();
			} else if (c == ']' && !stack.isEmpty() && stack.peek() == '[') {
				stack.pop();
			} else {
				return false; // If the character doesn't match or the stack is empty
			}
		}

		return stack.isEmpty();
	}

//	APPROACH - 2
	public boolean isValid2(String s) {
		Stack<Character> brackets = new Stack<>();
		Map<Character, Character> bracketLookup = new HashMap<>(3);

		bracketLookup.put(')', '(');
		bracketLookup.put('}', '{');
		bracketLookup.put(']', '[');

		for (int i = 0; i < s.length(); i++) {
			char c = s.charAt(i);
			if (bracketLookup.containsKey(c)) {
				if (!brackets.isEmpty() && bracketLookup.get(c).equals(brackets.peek())) {
					brackets.pop();
				} else {
					return false;
				}
			} else {
				brackets.push(c);
			}
		}

		return brackets.isEmpty();
	}
}
