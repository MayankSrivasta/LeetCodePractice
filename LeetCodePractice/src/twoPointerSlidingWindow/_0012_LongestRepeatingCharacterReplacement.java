package twoPointerSlidingWindow;

import java.util.HashMap;
import java.util.Map;

public class _0012_LongestRepeatingCharacterReplacement {

//	using hashmap
	public int characterReplacement1(String s, int k) {
		int left = 0;
		int maxLength = 0;
		int maxRepeatCount = 0;
		int len = s.length();
		Map<Character, Integer> map1 = new HashMap<>();

		for (int right = 0; right < len; right++) {

			char curr = s.charAt(right);
			map1.put(curr, map1.getOrDefault(curr, 0) + 1);

			maxRepeatCount = Math.max(maxRepeatCount, map1.get(curr));

			int nonrepeat = (right - left + 1) - maxRepeatCount;

			if (nonrepeat > k) {
				map1.put(s.charAt(left), map1.get(s.charAt(left)) - 1);
				left++;
			}

			maxLength = Math.max(maxLength, right - left + 1);

		}
		return maxLength;
	}

	public static int characterReplacement(String s, int k) {

		// Make an array of size 26...
		int[] arr = new int[26];
		// Initialize largestCount, maxlen & left pointer...

		int largestCount = 0, left = 0, maxlen = 0;
		// Traverse all characters through the loop...

		for (int right = 0; right < s.length(); right++) {

			arr[s.charAt(right) - 'A']++;
			// Get the largest count of a single, unique character in the current window...

			largestCount = Math.max(largestCount, arr[s.charAt(right) - 'A']);
			// We are allowed to have at most k replacements in the window...
			// So, if max character frequency + distance between left and right is greater
			// than
			// k...
			// this means we have considered changing more than k charactres. So time to
			// shrink window...
			// Then there are more characters in the window than we can replace, and we need
			// to shrink the window...

			int nonRepeatingCharacter = right - left + 1 - largestCount;
			if (nonRepeatingCharacter > k) { // The main equation is: right - left + 1 - largestCount...
				arr[s.charAt(left) - 'A']--;
				left++;
			}

			// Get the maximum length of repeating character...
			maxlen = Math.max(maxlen, right - left + 1); // right - left + 1 = size of the current window...

		}
		return maxlen; // Return the maximum length of repeating character...
	}

	public static void main(String[] args) {
		String s = "ABAB";
		int k = 2;
		int result = characterReplacement(s, k);
		System.out.println("Output: " + result);
	}

}
