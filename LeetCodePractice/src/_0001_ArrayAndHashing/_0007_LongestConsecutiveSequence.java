package _0001_ArrayAndHashing;

import java.util.HashSet;
import java.util.Set;

public class _0007_LongestConsecutiveSequence {

//	neetcode.io website solution
	public static int longestConsecutive(int[] nums) {
		Set<Integer> numSet = new HashSet<>();
		for (int num : nums) {
			numSet.add(num);
		}

		int longest = 0;

		for (int n : numSet) {
			// Only start counting if n is the start of a sequence because if the no. is in
			// the middle then it will be unnecessary iteration of numbers
//			the while loop can be avoided for numbers that are already part of a sequence, which reduces unnecessary checks.
//			Avoid Redundant Searches:
//				The if (!numSet.contains(n - 1)) check ensures that you only start counting when you find the beginning of a sequence. This avoids unnecessary work for numbers that are in the middle of a sequence.
			if (!numSet.contains(n - 1)) {
				int length = 1;
				while (numSet.contains(n + length)) {
					length++;
				}
				longest = Math.max(length, longest);
			}
		}
		return longest;
	}

	public static void main(String args[]) {
		System.out.println(longestConsecutive(new int[] { 2, 20, 4, 10, 3, 4, 5 }));
	}
}
