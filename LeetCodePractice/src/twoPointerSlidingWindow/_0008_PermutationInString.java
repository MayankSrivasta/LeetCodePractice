package twoPointerSlidingWindow;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class _0008_PermutationInString {

//	Using HashMap
	public boolean checkInclusion(String s1, String s2) {
		Map<Character, Integer> s1hash = new HashMap<>();
		Map<Character, Integer> s2hash = new HashMap<>();
		int s1len = s1.length();
		int s2len = s2.length();

		if (s1len > s2len) {
			return false;
		}

		int left = 0;
		int right = 0;

		while (right < s1len) {
			char charS1 = s1.charAt(right);
			char charS2 = s2.charAt(right);

			s1hash.put(charS1, s1hash.getOrDefault(charS1, 0) + 1);
			s2hash.put(charS2, s2hash.getOrDefault(charS2, 0) + 1);

			right++;
		}
		right--; // To point right to the end of the window

		while (right < s2len) {
			if (s1hash.equals(s2hash)) {
				return true;
			}

			right++;

			if (right != s2len) {
				char charS2Right = s2.charAt(right);
				s2hash.put(charS2Right, s2hash.getOrDefault(charS2Right, 0) + 1);
			}

			char charS2Left = s2.charAt(left);
			s2hash.put(charS2Left, s2hash.get(charS2Left) - 1);

			if (s2hash.get(charS2Left) == 0) {
				s2hash.remove(charS2Left);
			}

			left++;
		}

		return false;
	}

//	Using Array
	public boolean checkInclusion2(String s1, String s2) {
		int[] s1hash = new int[26];
		int[] s2hash = new int[26];
		int s1len = s1.length();
		int s2len = s2.length();

		if (s1len > s2len) {
			return false;
		}

		int left = 0;
		int right = 0;

		while (right < s1len) {
			s1hash[s1.charAt(right) - 'a']++;
			s2hash[s2.charAt(right) - 'a']++;
			right++;
		}

//		what is the purpose of this line
		right--; // To point right to the end of the window

		while (right < s2len) {
			if (Arrays.equals(s1hash, s2hash))
				return true;

			right++;
			
//		below line is just incrementing the value of the next character from S2 string into the sliding window.
			if (right != s2len)
				s2hash[s2.charAt(right) - 'a']++;

//		below line is just decrementing/removing the value from the starting of the sliding window
			s2hash[s2.charAt(left) - 'a']--;
			left++;
		}

		return false;
	}
}
