package _0002_TwoPointerSlidingWindow;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class _0023_PartitionLabels {

//	MY SOLUTION - but I should improve my code in hashing with array concept
	public List<Integer> partitionLabels2(String s) {

		List<Integer> list = new ArrayList();
		int map[] = new int[128];
		int n = s.length();

//	        this hashing concept should be improved as what given in below method
		for (int i = 0; i < n; i++)
			map[s.charAt(i)] = i;

//		below codes should be used
//		int[] map = new int[26];
//		for (int i = 0; i < arr.length; i++) {
//			map[arr[i] - 'a'] = i;
//		}

		int i = 0;
		int maxOcc = 0;
		for (int j = 0; j < n; j++) {
			maxOcc = Math.max(maxOcc, map[s.charAt(j)]);
			if (maxOcc == j) {
				list.add(j - i + 1);
				i = j + 1;
			}
		}
		return list;
	}

//	ERIC PROGRAMMIGN SOLUTION
	public List<Integer> partitionLabels(String S) {
		List<Integer> res = new LinkedList<>();
		char[] arr = S.toCharArray();
		// 1. Last appear character index save onto a table
		int[] map = new int[26];
		for (int i = 0; i < arr.length; i++) {
			map[arr[i] - 'a'] = i;
		}

		// 2. Define L and R
		int L = 0;
		int maxLastAppearIndex = 0;

		for (int R = 0; R < arr.length; R++) {
			// Current Character Last appear index
			int curLastAppearIndex = map[arr[R] - 'a'];

			// Update the max last appear char index
			maxLastAppearIndex = Math.max(maxLastAppearIndex, curLastAppearIndex);

			if (maxLastAppearIndex == R) {
				int len = R - L + 1;
				res.add(len);
				L = R + 1;
			}
		}
		return res;
	}

}