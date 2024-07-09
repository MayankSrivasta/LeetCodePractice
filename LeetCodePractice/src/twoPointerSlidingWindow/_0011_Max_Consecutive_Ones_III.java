package twoPointerSlidingWindow;

public class _0011_Max_Consecutive_Ones_III {

//	https://leetcode.com/problems/max-consecutive-ones-iii/description/

	/*
	 * Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2 Output: 6 Explanation:
	 * [1,1,1,0,0,1,1,1,1,1,1] Bolded numbers were flipped from 0 to 1. The longest
	 * subarray is underlined.
	 */

//	APPROACH - 1
	public static int longestOnes(int[] nums, int k) {

		int left = 0;
		int maxCons = 0;

		for (int right = 0; right < nums.length; right++) {

//			Inside the loop, decrement k by 1 - nums[right]. 
//			The expression 1 - nums[right] will be 0 if nums[right] is 1, 
//			and 1 if nums[right] is 0. This effectively counts the number of zeros encountered in the current window.

//			in given array since we have 2 intergers so its equation can be created to figure out whether its ones or zeros
//			& accordingly the values can be easily changes in an array. so that's why we have created an equation below
//			to change the values of the given array into 0's, 1's
			k -= 1 - nums[right];
			if (k < 0) {

//				If k is negative, we increment k by 1 - nums[left] and increment the left pointer. 
//				This step effectively "slides" the window to the right by removing elements from the left side of the window.
				// Adjust k by adding 1 when nums[left] is 0 (as we're moving the window to the
				// right).

				k += 1 - nums[left];

				left++;
			} else {
				maxCons = Math.max(maxCons, right - left + 1);
			}
		}

		return maxCons;
	}

//	APPROACH - 2
//	another appraoch from Nick White, below one is bit easier to understand
//	https://www.youtube.com/watch?v=97oTiOCuxho&t=311s

//	this approach is the faster execution time
	public static int longestOnes2(int[] A, int k) {
		int i = 0;
		int j = 0;
		while (j < A.length) {
			if (A[j] == 0)
				k--;

			if (k < 0) {
				if (A[i] == 0)
					k++;
				i++;
			}

			j++;
		}
		return j - i;
	}

//	APPROACH - 3
//	above one same approach just with using variable COUNT also
	public int longestOnes4(int[] nums, int k) {
		int i = 0, j = 0, count = 0;

		for (j = 0; j < nums.length; j++) {
			if (nums[j] == 0)
				count++;
			if (count > k) {
				if (nums[i] == 0)
					count--;
				i++;
			}
		}
		return j - i;
	}

//	nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2

	public static void main(String args[]) {
		System.out.println(longestOnes2(new int[] { 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0 }, 2));
	}

//	this approach is much more easier, because here we stops the increment of j untill we get the 1st i'th position
//	of 0's
//	

//	APPROACH - 4
	public static int longestOnes3(int[] nums, int k) {
//		https://www.youtube.com/watch?v=ROuOZongV6I&list=PL1MJrDFRFiKZYea2EAfuNJ9aosbpIlAf5&index=5

//		Ayushi Sharma easy solution
//		https://www.youtube.com/watch?v=Gl-8HLvV8bc&t=141s

		int zerocount = 0, i = 0;
		int result = 0;

		for (int j = 0; j < nums.length; j++) {
			if (nums[j] == 0)
				zerocount++;

			while (zerocount > k) {
				if (nums[i] == 0)
					zerocount--;
				i++;
			}
			result = Math.max(result, j - i + 1);
		}

		return result;
	}
}
