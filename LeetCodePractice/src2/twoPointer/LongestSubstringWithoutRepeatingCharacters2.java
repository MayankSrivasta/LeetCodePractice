package twoPointer;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

public class LongestSubstringWithoutRepeatingCharacters2 {

	public static void main(String args[]) {

		System.out.println(withHashMap("abcabcbb"));
	}

//	Using MAP
//	this only returns the length of the substring
	public static int withHashMap(String str) {

		Map<Character, Integer> hm = new HashMap<>();
		int i = 0, ans = 0;
		int len = str.length();
		for (int j = 0; j < len; j++) {
			char ch = str.charAt(j);
			if (hm.containsKey(ch))
				;
			i = Math.max(hm.get(ch) + 1, i);

			hm.put(str.charAt(j), j);
			ans = Math.max(ans, j - i + 1);
		}

		return ans;
	}

//	Using SET
//	below code could return the substring characters as it maintains the substring
	public int withSet(String str) {
		int ans = 0, j = 0, i = 0;

		Set<Character> set = new HashSet<>();
		while (j < str.length()) {
			if (!set.contains(str.charAt(j))) {
				set.add(str.charAt(j));
				j++;
				ans = Math.max(ans, set.size());
			} else {
				set.remove(str.charAt(i));
				i++;
			}
		}
		return ans;
	}

//	from LeetCode Submissions -> more easy to understand
	public int lengthOfLongestSubstring(String str) {

		int a = 0;
		int b = 0;
		int max = 0;
		Set<Character> set = new HashSet<>();
		while (b < str.length()) {
			if (!set.contains(str.charAt(b))) {
				set.add(str.charAt(b));
				b++;
				// the reason for below code is that the size of the set/substring will increase
				// & decrease but we have to always remember the maximum size of the substring
				max = Math.max(set.size(), max);
			} else {
				set.remove(str.charAt(a));
				a++;
			}
		}
		return max;
	}

}
