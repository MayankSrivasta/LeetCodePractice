package _0002_TwoPointerSlidingWindow;

import java.util.HashSet;
import java.util.Set;

public class _0027_MaximumErasureValue {

//	https://www.youtube.com/watch?v=7YqscdGIS6Y&list=PLPyD8bF-abztStd_A38_AlLkSlMwooi8H&index=5

//	https://leetcode.com/problems/maximum-erasure-value/
	
	public int maximumUniqueSubarray(int[] nums) {

		Set<Integer> set = new HashSet();
		int i = 0, j = 0, sum = 0;
		int maxSum = 0;
		for (j = 0; j < nums.length; j++) {

			while (set.contains(nums[j])) {
				set.remove(nums[i]);
				sum -= nums[i++];
			}

			set.add(nums[j]);
			sum += nums[j];
			maxSum = Math.max(maxSum, sum);
		}
		return maxSum;
	}

}
