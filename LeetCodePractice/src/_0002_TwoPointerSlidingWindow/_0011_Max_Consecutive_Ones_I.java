package _0002_TwoPointerSlidingWindow;

public class _0011_Max_Consecutive_Ones_I {
	
	public static int findMaxConsecutiveOnes(int[] nums) {
		int counter = 0;
		int maxCount = 0;
		for (int i = 0; i < nums.length; i++) {
			if (nums[i] == 0)
				counter = 0;

			if (nums[i] == 1) {
				counter++;
				maxCount = maxCount > counter ? maxCount : counter;
			}

		}
		return maxCount;
	}
}
