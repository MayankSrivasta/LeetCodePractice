package twoPointer;

import java.util.HashMap;
import java.util.Map;

public class _0000_TestClass {

	public int longestSubstringWithoutRepeatingCharacters(String str) {

		int i = 0;
		int max = 0;
		Map<Character, Integer> hm = new HashMap();
		for (int j = 0; j < str.length(); j++) {
			char ch = str.charAt(j);

			if (hm.containsKey(ch))
				i = Math.max(i, hm.get(ch) + 1);

			hm.put(ch, j);
			max = Math.max(max, j - i + 1);

		}

		return max;
	}
}
