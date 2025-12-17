package _0002_TwoPointerSlidingWindow;

public class _0021_SquaresOfASortedArray {

//	Input: nums = [-4,-1,0,3,10]
//		  Output: [0,1,9,16,100]

	public int[] sortedSquares(int[] nums) {
		int[] res = new int[nums.length];
		int left = 0;
		int right = nums.length - 1;

		for (int i = nums.length - 1; i >= 0; i--) {
			if (Math.abs(nums[left]) > Math.abs(nums[right])) {
				res[i] = nums[left] * nums[left];
				left++;
			} else {
				res[i] = nums[right] * nums[right];
				right--;
			}
		}
		return res;
	}

//	eric programming solution
	public int[] sortedSquares2(int[] nums) {
		int left = 0, n = nums.length, right = n - 1, index = n - 1;

		int[] res = new int[n];

		while (0 <= index) {
			int leftNum = nums[left] * nums[left];
			int rightNum = nums[right] * nums[right];
			if (leftNum < rightNum) {
				res[index--] = rightNum;
				right--;
			} else {
				left++;
				res[index--] = leftNum;
			}
		}
		return res;
	}

}
