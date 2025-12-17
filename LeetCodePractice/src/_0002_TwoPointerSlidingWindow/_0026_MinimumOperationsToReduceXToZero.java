package _0002_TwoPointerSlidingWindow;

import java.util.HashMap;
import java.util.Map;

// this question might be similar to MAXIMUM POINTS YOU CAN OBTAINS FROM CARDS
public class _0026_MinimumOperationsToReduceXToZero {

	public int minOperations(int[] nums, int x) {
		int sum = 0, n = nums.length;
		for (int num : nums)
			sum += num;
		int target = sum - x;
		int currSum = 0, maxLen = 0;
		int i = 0; // starting index of subarray
		boolean found = false;

		for (int j = 0; j < n; j++) {
			currSum += nums[j];

			// shrinking our window
			while (i <= j && currSum > target) {
				currSum -= nums[i];
				i += 1;
			}
			if (currSum == target) {
				found = true;
				maxLen = Math.max(maxLen, j - i + 1);
			}
		}
		return found ? n - maxLen : -1;
	}

//	AlgorithmsMadeEasy youtube
//	https://www.youtube.com/watch?v=3p2fBvxrVQA
	// Using Prefix Sum
	public int minOperations2(int[] nums, int x) {
		int target = -x;
		for (int i : nums)
			target += i;
		if (target == 0)
			return nums.length;
		Map<Integer, Integer> map = new HashMap<>();
		map.put(0, -1);
		int res = -1, sum = 0;

		for (int i = 0; i < nums.length; i++) {
			sum += nums[i];
			if (map.containsKey(sum - target)) {
				res = Math.max(res, i - map.get(sum - target));
			}
			map.put(sum, i);
		}

		return res == -1 ? -1 : nums.length - res;
	}

	// Using Siding Window

	public int minOperations3(int[] nums, int x) {
		int target = -x;
		for (int i : nums)
			target += i;
		if (target == 0)
			return nums.length;

		if (target < 0)
			return -1;

		int res = -1, sum = 0, i = 0;

		for (int j = 0; j < nums.length; j++) {
			sum += nums[j];
			while (sum > target) {
				sum -= nums[i++];
			}
			if (sum == target) {
				res = Math.max(res, j - i + 1);
			}
		}

		return res == -1 ? -1 : nums.length - res;
	}
}
