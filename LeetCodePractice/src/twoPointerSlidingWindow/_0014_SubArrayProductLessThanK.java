package twoPointerSlidingWindow;

public class _0014_SubArrayProductLessThanK {

	public static int numSubarrayProductLessThanK(int[] nums, int k) {
		int i = 0, n = nums.length, product = 1, result = 0;
	
		for (int j = 0; j < n; j++) {
			product = product * nums[j];
			while (i <= j && product >= k) {
				product = product / nums[i];
				i++;
			}
			result += j - i + 1;
		}
		return result;
	}

	public static void main(String args[]) {
		System.out.println(numSubarrayProductLessThanK(new int[] { 10, 5, 2, 6 }, 100));
	}

}