package leetCode;

import java.util.ArrayList;
import java.util.List;

public class StringFormation {

	public static int numWays(List<String> words, String target) {
		long dp[] = new long[target.length()];
		long mod = 1000000000 + 7;

		String[] w = new String[words.size()];

		for (int i = 0; i < words.size(); i++)
			w[i] = words.get(i);

		for (int i = 0; i < w[0].length(); i++) {
			int[] freq = new int[26];
			for (String word : w) {
				freq[word.charAt(i) - 'a']++;
			}

			for (int j = Math.min(i, target.length() - 1); j >= 0; j--) {
				if (freq[target.charAt(j) - 'a'] > 0) {
					dp[j] += (j == 0) ? freq[target.charAt(j) - 'a'] : dp[j - 1] * freq[target.charAt(j) - 'a'];
					dp[j] %= mod;
				}
			}
		}
		return (int) dp[dp.length - 1];
	}

	public static int findMaxSubsegmentsCount(List<Integer> arr) {

		int nums[] = new int[arr.size()];

		for (int i = 0; i < arr.size(); i++) {
			nums[i] = arr.get(i);
		}

		int max = 0;
		int chunks_count = 0;
		for (int i = 0; i < nums.length; i++) {
			max = Math.max(max, nums[i]);
			if (i == max) {
				chunks_count++;
			}
		}
		return chunks_count;
	}

	public static int findMaxSubsegmentsCount2(List<Integer> arr) {

		int n = arr.size();
		int nums[] = new int[arr.size()];

		for (int i = 0; i < arr.size(); i++) {
			nums[i] = arr.get(i);
		}

		int max_so_far = 0;

		int max_ending_here = 0;

		for (int i = 0; i < n; i++) {
			max_ending_here = max_ending_here + nums[i];

			max_ending_here = Math.max(max_ending_here, 0);

			max_so_far = Math.max(max_so_far, max_ending_here);
		}

		return max_so_far;
	}

	public static void main(String args[]) {

		List<Integer> list = new ArrayList();

		list.add(2);
		list.add(10);
		list.add(5);
		list.add(9);

		System.out.println(maxChunksToSorted(list));
	}

	public static int maxChunksToSorted(List<Integer> arr) {

		int n = arr.size();
		int nums[] = new int[arr.size()];

		for (int i = 0; i < arr.size(); i++) {
			nums[i] = arr.get(i);
		}

		int[] rightMax = new int[nums.length + 1];
		int[] leftMin = new int[nums.length + 1];

		int max = 0;
		int min = Integer.MAX_VALUE;

		for (int i = 0; i < leftMin.length - 1; i++) {
			max = Math.max(max, nums[i]);
			rightMax[i] = max;

		}

		leftMin[nums.length] = Integer.MAX_VALUE;

		for (int i = leftMin.length - 2; i >= 0; i--) {
			min = Math.min(min, nums[i]);
			leftMin[i] = min;
		}

		int chunk = 0;
		for (int i = 0; i < rightMax.length - 1; i++) {
			if (rightMax[i] <= leftMin[i + 1]) {
				chunk++;
			}
		}

		return chunk;
	}

}
