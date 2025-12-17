package _0002_TwoPointerSlidingWindow;

import java.util.HashMap;
import java.util.Map;

//BELOW IS THE TEMPATE TO SOLVE MOST OF THE SLIDING WINDOW QUESTIONS

public class _0016_MinimumWindowSubstring {

//	BELOW IS THE SOLUTION THAT I SOLVED ON LEETCODE
//	https://www.youtube.com/watch?v=yT5nzi9f_T4&list=PL1MJrDFRFiKZYea2EAfuNJ9aosbpIlAf5&index=10
	public String minWindow3(String s, String t) {

		int map[] = new int[128];
		int i = 0, j = 0, minLength = Integer.MAX_VALUE;
		char[] sArr = s.toCharArray();
		char[] tArr = t.toCharArray();
		String str = "";
		int count = 0;

		for (char ch : tArr)
			map[ch]++;

		for (j = 0; j < s.length(); j++) {
			// here is most important thing, any element index will be greater than 0 only
			// in case if its value is already more than 1 in given by t & s, so it should
			// be
			// greater than 0.
			if (map[sArr[j]] > 0)
				count++;
			map[sArr[j]]--;

			while (count == t.length()) {
				if (minLength > j - i + 1) {
					minLength = j - i + 1;
					str = s.substring(i, j + 1);
				}

//				decrementing the counter, 
				if (map[sArr[i]] == 0)
					count--;

				map[sArr[i]]++;
				i++;
			}
		}
		return str;
	}

//	https://www.youtube.com/watch?v=yT5nzi9f_T4&list=PL1MJrDFRFiKZYea2EAfuNJ9aosbpIlAf5&index=8
//	eric programming
	public String minWindow(String s, String t) {

		int[] map = new int[128];
		char[] arr = s.toCharArray();

		// Set up the table
		for (char cur : t.toCharArray()) {
			map[cur]++;
		}

		int countAllCharInT = 0;
		int left = 0, n = arr.length, right = 0;
		int minLen = Integer.MAX_VALUE;
		String minLenStr = "";

		while (right < n) {
			// Expand the window
			map[arr[right]]--;
			if (0 <= map[arr[right]]) {
				countAllCharInT++;
			}

			// Shrink the window if current window contains all the char in t
			while (countAllCharInT == t.length()) {
				// Update the minLen
				if (minLen > right - left + 1) {
					minLen = right - left + 1;
					minLenStr = s.substring(left, right + 1);
				}

				// Shrink the window
				map[arr[left]]++;
				if (0 < map[arr[left]]) {
					countAllCharInT--;
				}
				left++;
			}

			right++;
		}

		return minLenStr;
	}

	// sliding window
	public String minWindow2(String s, String t) {
		int[] map = new int[128];

		// Fill the map with the frequency of characters in t
		for (char x : t.toCharArray()) {
			map[x]++;
		}

		int matched = 0;
		int start = 0;
		int minLen = s.length() + 1;
		int subStr = 0;
		int required = t.length();

		for (int endWindow = 0; endWindow < s.length(); endWindow++) {
			char right = s.charAt(endWindow);
			if (map[right] > 0) {
				matched++;
			}
			map[right]--;

			while (matched == required) {
				if (minLen > endWindow - start + 1) {
					minLen = endWindow - start + 1;
					subStr = start;
				}
				char left = s.charAt(start++);
				if (map[left] == 0) {
					matched--;
				}
				map[left]++;
			}
		}

		return minLen > s.length() ? "" : s.substring(subStr, subStr + minLen);
	}

	// sliding window
//	neetCode java solution
	public String minWindowUsingMap(String s, String t) {
		HashMap<Character, Integer> map = new HashMap<>();

		for (char x : t.toCharArray()) {
			map.put(x, map.getOrDefault(x, 0) + 1);
		}

		int matched = 0;
		int start = 0;
		int minLen = s.length() + 1;
		int subStr = 0;
//		expanding
		for (int endWindow = 0; endWindow < s.length(); endWindow++) {
			char right = s.charAt(endWindow);
			if (map.containsKey(right)) {
				map.put(right, map.get(right) - 1);
				if (map.get(right) == 0)
					matched++;
			}

//			shrinking
			while (matched == map.size()) {
				if (minLen > endWindow - start + 1) {
					minLen = endWindow - start + 1;
					subStr = start;
				}
				char deleted = s.charAt(start++);
				if (map.containsKey(deleted)) {
					if (map.get(deleted) == 0)
						matched--;
					map.put(deleted, map.get(deleted) + 1);
				}
			}
		}
		return minLen > s.length() ? "" : s.substring(subStr, subStr + minLen);
	}
}
