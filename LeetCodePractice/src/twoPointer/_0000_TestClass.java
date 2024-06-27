package twoPointer;

import java.util.HashMap;
import java.util.Map;

public class _0000_TestClass {

	public int longestSubstringWithoutRepeatingCharacters(String str) {

//		a b c a b c b b
//		i     j

//		set

//		a b c c b a b b
//      i     j
		int i = 0, j = 0, max = 0;

		Map<Character, Integer> hm = new HashMap();

		for (j = 0; j < str.length(); j++) {
			if (hm.containsKey(str.charAt(j)))
				i = Math.max(i, hm.get(str.charAt(j)) + 1);

			hm.put(str.charAt(j), j);
			max = Math.max(max, j - i + 1);

		}

		return max;

	}
}
