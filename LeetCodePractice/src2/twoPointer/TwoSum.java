package twoPointer;

import java.util.HashMap;
import java.util.Map;

public class TwoSum {
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
