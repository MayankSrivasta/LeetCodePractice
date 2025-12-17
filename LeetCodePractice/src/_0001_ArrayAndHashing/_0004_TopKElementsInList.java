package _0001_ArrayAndHashing;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class _0004_TopKElementsInList {

//	neetcode solution
	public static int[] topKFrequent(int[] nums, int k) {

		Map<Integer, Integer> count = new HashMap<>();
		for (int n : nums) {
			count.put(n, count.getOrDefault(n, 0) + 1);
		}

//		bucket sort
		List<Integer>[] freq = new List[nums.length + 1];
		for (int i = 0; i < freq.length; i++) {
			freq[i] = new ArrayList<>();
		}

		for (Map.Entry<Integer, Integer> entry : count.entrySet()) {
			freq[entry.getValue()].add(entry.getKey());
		}

		int[] res = new int[k];
		int index = 0;
//		the reason for calculating in reverse, because obviously the frequency is going to be
//		hight from the left -> right iteration
		for (int i = freq.length - 1; i > 0 && index < k; i--) {
			for (int n : freq[i]) {
				res[index++] = n;
				if (index == k) {
					return res;
				}
			}
		}
		return res;
	}

	public static void main(String args[]) {
		System.out.println(topKFrequent(new int[] { 1, 2, 3, 4, 5, 6 }, 2));
	}

}
