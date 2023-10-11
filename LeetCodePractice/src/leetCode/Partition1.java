package leetCode;

import java.util.ArrayList;
import java.util.List;

public class Partition1 {

	static int findSplitPoint(int arr[], int n) {

		int leftSum = 0;

		for (int i = 0; i < n; i++)
			leftSum += arr[i];

		int rightSum = 0;

		for (int i = n - 1; i >= 0; i--) {
			rightSum += arr[i];

			leftSum -= arr[i];

			if (rightSum == leftSum)
				return i;
		}

		return -1;
	}

	static long printTwoParts(int arr[], int n) {

//		for(int i = 0; i < list.size(); i++)
//		{
//			
//		}

		int splitPoint = findSplitPoint(arr, n);

		if (splitPoint == -1 || splitPoint == n) {
			return -1;
		}

		List<Integer> list1 = new ArrayList();
		List<Integer> list2 = new ArrayList();

		int m = 0, k = 0;
		for (int i = 0; i < n; i++) {
			if (splitPoint <= i) {
				list1.add(arr[i]);

			} else {
				list2.add(arr[i]);

			}

		}

		System.out.println(list1);
		System.out.println(list2);

		long sum1 = 0;
		long sum2 = 0;

		for (int a : list1) {
			a *= a;
			sum1 = a;
		}
		for (int a : list2) {
			a *= a;
			sum2 = a;
		}
		return sum1 + sum2;
	}

	// Driver program
	public static void main(String[] args) {

		int arr[] = { 1, 2, 3, 2 };
		int n = arr.length;

		printTwoParts(arr, n);

	}
}
