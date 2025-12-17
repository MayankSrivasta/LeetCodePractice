package _0004_Stack;

import java.util.Arrays;
import java.util.Stack;

public class _0005_DailyTemperatures {

//	Neetcode.io solution
	public static int[] dailyTemperatures3(int[] temperatures) {
		int[] ans = new int[temperatures.length];
		Stack<Integer> stack = new Stack<>();
		for (int currDay = 0; currDay < temperatures.length; currDay++) {
			while (!stack.isEmpty() && temperatures[currDay] > temperatures[stack.peek()]) {
				int prevDay = stack.pop();
				ans[prevDay] = currDay - prevDay;
			}
			stack.add(currDay);
		}
		return ans;
	}

	public static void main(String args[]) {
		System.out.println(Arrays.toString(dailyTemperatures3(new int[] { 73, 74, 75, 71, 69, 72, 76, 73 })));
	}

}
