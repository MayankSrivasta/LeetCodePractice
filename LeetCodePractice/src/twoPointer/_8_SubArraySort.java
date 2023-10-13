package twoPointer;

public class _8_SubArraySort {

//	Question/Answer Video link
//	https://www.udemy.com/course/cpp-data-structures-algorithms-levelup-prateek-narang/learn/lecture/25191108#overview

//	given - [10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60]
//	subarray lies between indexes 3 and 8

	public static boolean outOfOrder(int[] arr, int i) {
		int x = arr[i];
		if (i == 0) {
			return x > arr[1];
		}
		if (i == arr.length - 1) {
			return x < arr[i - 1];
		}
		return x > arr[i + 1] || x < arr[i - 1];

	}

	public static int[] subarraySort(int[] arr) {

		int smallest = Integer.MAX_VALUE;
		int largest = Integer.MIN_VALUE;

		for (int i = 0; i < arr.length; i++) {
			int x = arr[i];

			if (outOfOrder(arr, i)) {
				smallest = Math.min(smallest, x);
				largest = Math.max(largest, x);
			}
		}

		// next step find the right index where smallest and largest lie (subarray) for
		// out solution
		if (smallest == Integer.MAX_VALUE) {
			return new int[] { -1, -1 };
		}

		int left = 0;
		while (smallest >= arr[left]) {
			left++;
		}
		int right = arr.length - 1;
		while (largest <= arr[right]) {
			right--;
		}

		return new int[] { left, right };

	}

	public static void main(String[] args) {
		int[] ar = { 1, 2, 3, 4, 5, 8, 6, 7, 9, 10, 11 };
		int[] p = subarraySort(ar);
		System.out.println(p[0] + " and " + p[1]);
	}

}
