package _0002_TwoPointerSlidingWindow;

import java.util.HashMap;
import java.util.Map;

public class _0030_LengthOfLongestSubarrayWithAtMostKFrequency_2958 {

	// Time Complexity - O(N)
	// Space Complexity : O(N)

	public int maxSubarrayLength(int[] nums, int k) {

		int i = 0, j = 0, max = 0;
		Map<Integer, Integer> hm = new HashMap();
		for (j = 0; j < nums.length; j++) {

			hm.put(nums[j], hm.getOrDefault(nums[j], 0) + 1);

			while (hm.get(nums[j]) > k)
				hm.put(nums[i], hm.get(nums[i++]) - 1);

			max = Math.max(max, j - i + 1);
		}

		return max;
	}
}
