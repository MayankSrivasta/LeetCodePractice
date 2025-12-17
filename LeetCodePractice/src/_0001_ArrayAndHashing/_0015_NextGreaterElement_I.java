package _0001_ArrayAndHashing;

import java.util.HashMap;
import java.util.Map;
import java.util.Stack;

public class _0015_NextGreaterElement_I {

	public int[] nextGreaterElement(int[] nums1, int[] nums2) {

		int[] res = new int[nums1.length];
		int counter = 0;

		for (int i : nums1) {
			res[counter++] = ans(i, nums2);
		}

		return res;

	}

	private int ans(int i, int[] nums) {
		for (int n = 0; n < nums.length; n++) {
			if (nums[n] == i) {
				for (int j = n + 1; j < nums.length; j++) {
					if (nums[j] > i)
						return nums[j];
				}
			}
		}
		return -1;
	}

//	USING BOTH STACK & HASHMAP
//	n1[] = [4, 1, 2]
//	n2[] = [2, 1, 3, 4]
//	monotonic stack - strictly increasing or decreasing order
	public static int[] nextGreaterElement2(int[] findNums, int[] nums) {
		Map<Integer, Integer> map = new HashMap<>();
		Stack<Integer> stack = new Stack<>();
		for (int num : nums) {
			while (!stack.isEmpty() && stack.peek() < num) {
				int p = stack.pop();
				map.put(p, num);
			}
			stack.push(num);
		}
		for (int i = 0; i < findNums.length; i++)
			findNums[i] = map.getOrDefault(findNums[i], -1);
		return findNums;
	}
}
