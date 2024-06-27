package twoPointerSlidingWindow;

import java.util.HashMap;
import java.util.Map;

//https://leetcode.com/problems/two-sum/
public class _0001_TwoSum {
	public int[] twoSum(int[] nums, int target) {
		Map<Integer, Integer> hm = new HashMap<>();

		for (int i = 0; i < nums.length; i++) {

			int k = target - nums[i];
			if (hm.containsKey(k)) {
				return new int[] { hm.get(k), i };
			}
			hm.put(nums[i], i);

		}
		return new int[] { -1, -1 };
	}
}
