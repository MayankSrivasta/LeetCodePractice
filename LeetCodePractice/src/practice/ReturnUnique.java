package practice;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Stack;

public class ReturnUnique {

	public static void main(String[] args) {

		System.out.println(countCharacters("   "));

	}

	public static Map<Character, Integer> countCharacters(String string) {
		HashMap<Character, Integer> map = null;

		return null;

	}

	static String isBalanced(String str) {
		Stack<Character> stack = new Stack<>();
		for (int i = 0; i < str.length(); i++) {
			if (str.charAt(i) == '(' || str.charAt(i) == '{' || str.charAt(i) == '[')
				stack.push(str.charAt(i));
			else {
				if (stack.isEmpty()) {
					return "No";
				} else {
					Character ch = stack.pop();
					if (ch == '{' && str.charAt(i) != '}') {
						return "No";
					} else if (ch == '(' && str.charAt(i) != ')') {
						return "No";
					} else if (ch == '[' && str.charAt(i) != ']') {
						return "No";
					}
				}
			}

		}
		if (stack.empty())
			return "Yes";
		else
			return "No";
	}

	public List<Integer> findPrimes(int b) {

		List<Integer> list = new ArrayList<>();

		if (b == 0) {
			return new ArrayList<>();
		}

		if (b <= 2) {

			list.add(b);
			return list;
		}
		for (int i = 2; i <= b; i++) {

			// Skip 0 and 1 as they are
			// neither prime nor composite
			if (i == 1 || i == 0)
				continue;

			// flag variable to tell
			// if i is prime or not
			int flag = 1;

			for (int j = 2; j <= i / 2; ++j) {
				if (i % j == 0) {
					flag = 0;
					break;
				}
			}

			// flag = 1 means i is prime
			// and flag = 0 means i is not prime
			if (flag == 1)
				list.add(i);
		}
		return list;
	}

}
