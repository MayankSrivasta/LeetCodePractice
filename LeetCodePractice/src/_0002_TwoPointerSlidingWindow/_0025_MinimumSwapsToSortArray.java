package _0002_TwoPointerSlidingWindow;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

//input - 1, 5, 4, 3, 2
//output - 1 , 2, 3, 4, 5 -> 2 swaps

//input -  1, 5, 4, 3, 2
//output - 1, 2, 3, 4, 5 -> 2 swaps

//map  - 0, 1, 2, 3, 4
//values- 1, 5, 4, 2, 2

//	https://www.geeksforgeeks.org/minimum-number-swaps-required-sort-array/

public class _0025_MinimumSwapsToSortArray {

	public static void swap(int[] arr, int i, int j) {
		int temp = arr[i];
		arr[i] = arr[j];
		arr[j] = temp;
	}

	public static int minimumNumberOfSwaps(int[] arr, int n) {
		int ans = 0;

		int sortArr[] = Arrays.copyOf(arr, n);
		Arrays.sort(sortArr);

		Map<Integer, Integer> hm = new HashMap();

		for (int i = 0; i < arr.length; i++)
			hm.put(arr[i], i);

		for (int i = 0; i < arr.length; i++) {
			if (arr[i] != sortArr[i]) {
				ans++;

//				swapping
				int temp = sortArr[i];
				swap(arr, i, hm.get(temp));

//				updating HashMap with new indexes

				// 5
				hm.put(temp, sortArr[i]);

				// 2
				hm.put(sortArr[i], i);

			}
		}
		return ans;
	}

	public static void main(String[] args) {
//		input - 1, 5, 4, 3, 2
//		output - 1 , 2, 3, 4, 5 -> 2 swaps
		int[] arr = { 1, 5, 4, 3, 2 };
		int n = arr.length;
		System.out.println(minimumNumberOfSwaps(arr, n));
	}
}
