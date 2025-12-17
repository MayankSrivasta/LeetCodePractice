package _0001_ArrayAndHashing;

public class _0006_ProductOfArrayExceptSelf {

//	https://www.youtube.com/watch?v=bNvIQI2wAjk
//	CHECK NEETCODE.IO VIDEO TO UNDERSTAND THIS QUESION ELSE YOU WONT BE ABLE TO REVISE
//	THIS QUESTION AGAIN, IT WOULD BE DIFFICULT TO UNDERSTAND THIS QUESTION
	public static int[] productExceptSelf(int[] nums) {

		int[] arr = new int[nums.length];

		int right = 1, left = 1;

		for (int i = 0; i < nums.length; i++) {
			arr[i] = left;
			left *= nums[i];
		}

		for (int i = nums.length - 1; i >= 0; i--) {
			arr[i] *= right;
			right *= nums[i];
		}
		return arr;
	}

//	output -> 24, 12, 6, 8
	public static void main(String args[]) {
		for (int i : productExceptSelf(new int[] { 1, 2, 3, 4 }))
			System.out.print(i + " ");

	}
}
