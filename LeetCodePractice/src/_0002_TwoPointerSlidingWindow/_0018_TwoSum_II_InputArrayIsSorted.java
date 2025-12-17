package _0002_TwoPointerSlidingWindow;

public class _0018_TwoSum_II_InputArrayIsSorted {

//	https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

	public int[] twoSum(int[] nums, int target) {
		int n = nums.length - 1;
		int i = 0, j = n;

		while (i < j) {
			int sum = nums[i] + nums[j];
			if (sum > target) {
				j--;
			} else if (sum < target) {
				i++;
			} else {
				return new int[] { i + 1, j + 1 };
			}

		}
		return new int[] { -1, -1 };
	}
}