package _0004_Stack;

import java.util.Stack;

public class _0007_LargestRectangleInHistogram {

//	Solution from AlgorithmMadeEasy Youtube
	public static int largestRectangleArea(int[] h) {
		int n = h.length;
		int maxArea = 0;
		Stack<Integer> s = new Stack();
		for (int i = 0; i <= n; i++) {

			int currHeight = i == n ? 0 : h[i];
			// currHeight › h[top] ? push(i) : pop & find area
			while (!s.isEmpty() && currHeight < h[s.peek()]) {
				int top = s.pop();
				int width = s.isEmpty() ? i : i - s.peek() - 1;
				int area = h[top] * width;
				maxArea = Math.max(area, maxArea);
			}
			s.push(i);
		}
		return maxArea;
	}

	public static void main(String args[]) {
		System.out.println(largestRectangleArea(new int[] { 2, 1, 5, 6, 2, 3 }));
	}
}
