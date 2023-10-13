package twoPointer;

public class _10_MaximumSubArray {

//	https://leetcode.com/problems/maximum-subarray/description/
	
//	different solution link-  https://www.nileshblog.tech/leetcode-53-maximum-subarray/#google_vignette
//	sliding window, dynamic programming
//	there are multiple ways to solve this problem -> 
//	1. Kedane Approach
//	2. dynamic 
//	3. sliding window
//	4. divide & conquer - lengthy code

//	sliding window approach
	public int maxSubArray(int[] nums) {
		int maxSub = nums[0];
		int curSum = 0;

		for (int n : nums) {
			if (curSum < 0) {
				curSum = 0;
			}
			curSum += n;
			maxSub = Math.max(maxSub, curSum);
		}
		return maxSub;
	}

//	Kedane Algorithm Approach
	public int maxSubArray2(int[] arr) {
		int sum = 0;
		int maxi = arr[0];
		for (int i = 0; i < arr.length; i++) {
			sum = sum + arr[i];
			maxi = Math.max(maxi, sum);
			if (sum < 0) {
				sum = 0;
			}
		}
		return maxi;
	}

//	dynamic programming approach
	public int maxSubArray3(int[] nums) {
		int max_sum = nums[0];
		int max_ending_here = nums[0];

		for (int i = 1; i < nums.length; i++) {
			max_ending_here = Math.max(max_ending_here + nums[i], nums[i]);
			max_sum = Math.max(max_sum, max_ending_here);
		}

		return max_sum;
	}
}