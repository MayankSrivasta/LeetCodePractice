package twoPointerSlidingWindow;

public class _0009_MinimumSizeSubArraySum {

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
				ans = Math.min(ans, right + 1 - left);
//				it removes the leftMost element from the subArray/window
				sum -= nums[left++];
			}
		}
//		if the sum is never greater than the target then 
//		
		return (ans != Integer.MAX_VALUE) ? ans : 0;
	}

	public static void main(String args[]) {
		System.out.println(minSubArrayLen(7, new int[] { 2, 3, 1, 2, 4, 3 }));
	}

}
