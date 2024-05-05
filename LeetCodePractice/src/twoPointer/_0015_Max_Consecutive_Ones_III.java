package twoPointer;

public class _0015_Max_Consecutive_Ones_III {

//	https://leetcode.com/problems/max-consecutive-ones-iii/description/

	/*
	 * Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2 Output: 6 Explanation:
	 * [1,1,1,0,0,1,1,1,1,1,1] Bolded numbers were flipped from 0 to 1. The longest
	 * subarray is underlined.
	 */

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

	public static void main(String args[]) {
		System.out.println(longestOnes2(new int[] { 1, 1, 1, 0, 0, 0, 1, 1, 1}, 2));
	}

//	another appraoch from Nick White, below one is bit easier to understand
//	https://www.youtube.com/watch?v=97oTiOCuxho&t=311s
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

}

/*
 * Here's a step-by-step explanation of the code:
 * 
 * Initialize two pointers, left and right, to 0. These pointers will help keep
 * track of the current window of elements.
 * 
 * Initialize a variable maxCons to 0. This variable will store the maximum
 * length of consecutive ones encountered so far.
 * 
 * Start a loop that iterates through the nums array using the right pointer.
 * The loop continues until the right pointer reaches the end of the array.
 * 
 * Inside the loop, decrement k by 1 - nums[right]. The expression 1 -
 * nums[right] will be 0 if nums[right] is 1, and 1 if nums[right] is 0. This
 * effectively counts the number of zeros encountered in the current window.
 * 
 * Check if k becomes negative, indicating that we have encountered more zeros
 * than allowed in the current window. If k is negative, we need to adjust the
 * window to continue the search for a longer sequence of consecutive ones.
 * 
 * If k is negative, we increment k by 1 - nums[left] and increment the left
 * pointer. This step effectively "slides" the window to the right by removing
 * elements from the left side of the window.
 * 
 * If k is still non-negative (i.e., we haven't exceeded the allowed number of
 * flips), calculate the current length of consecutive ones in the window using
 * right - left + 1. Update maxCons with the maximum of its current value and
 * this calculated length.
 * 
 * Repeat the process by moving the right pointer to the right in the nums array
 * and continue checking for the longest sequence of consecutive ones with at
 * most k flips.
 * 
 * After the loop is complete, return the value of maxCons, which represents the
 * length of the longest sequence of consecutive ones with at most k flips
 * encountered in the entire array.
 * 
 */