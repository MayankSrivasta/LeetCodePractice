package twoPointerSlidingWindow;

public class _0009_MinimumSizeSubArraySum {
//	https://leetcode.com/problems/minimum-size-subarray-sum/description/
	
	public static int minSubArrayLen3(int s, int[] nums) {
        int n = nums.length;
		int ans = Integer.MAX_VALUE;
		int left = 0;
		int sum = 0;
//		2, 3, 1, 2, 4, 3
		int right = 0;
		while (right < n) {

			if (sum >= s) {
				ans = Math.min(ans, right - left + 1);
				sum -= nums[left++];
			} else {
				sum += nums[right];
				right++;
			}

		}

		return (ans != Integer.MAX_VALUE) ? ans : 0;
    }
	
	public static int minSubArrayLenMain(int target, int[] nums) {
		int minLength = Integer.MAX_VALUE;
		int i = 0, j = 0;
		int sum = 0;
		for (j = 0; j < nums.length; j++) {
			sum += nums[j];

			while (sum >= target) {
				minLength = Math.min(minLength, j - i + 1);
				sum -= nums[i];
				i++;
			}
		}
		return minLength == Integer.MAX_VALUE ? 0 : minLength;
	}

	public static int minSubArrayLen(int s, int[] nums) {
		int n = nums.length;
//		setting max length for the subArray
		int ans = Integer.MAX_VALUE;
		int left = 0;
		int sum = 0;
		for (int right = 0; right < n; right++) {
//			just keeps on adding the new element into the list
			sum += nums[right];
//			as soon as the sum is greater than the target sum the the elements from the 
//			left side needs to be removed.
			while (sum >= s) {
//				it calculates the length of the subArray/window
				ans = Math.min(ans, right - left + 1);
//				it removes the leftMost element from the subArray/window
				sum -= nums[left++];
			}
		}
//		if the sum is never greater than the target then 
//		
		return (ans != Integer.MAX_VALUE) ? ans : 0;
	}

	public static void main(String args[]) {
		System.out.println(minSubArrayLen3(7, new int[] { 2, 3, 1, 2, 4, 3 }));
	}


}
