package _0001_ArrayAndHashing;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class _0001_GroupAnagram {

//	learned from NeetCode.io
//	https://www.youtube.com/watch?v=vzdNOK2oB2E
	public static List<List<String>> groupAnagrams(String[] strs) {
		Map<String, List<String>> map = new HashMap<>();

		for (String s : strs) {
			int[] count = new int[26];

			for (char c : s.toCharArray()) {
				count[c - 'a']++;
			}

			StringBuilder sb = new StringBuilder();
			for (int i = 0; i < 26; i++) {
				sb.append('#');
				sb.append(count[i]);
			}
			
//			key would look like this
//			key = #1#0#0#0#1#0#0#0#0#0#0#0#0#0#0#0#0#0#0#1#0#0#0#0#0#0
			String key = sb.toString();

			if (!map.containsKey(key)) {
				map.put(key, new ArrayList<>());
			}
			map.get(key).add(s);
		}

		return new ArrayList<>(map.values());
	}

//	-------------------------------------------------------------------------
//	this one uses sorting which increases the time complexity

	public static List<List<String>> groupAnagrams2(String[] strs) {
		Map<String, List<String>> map = new HashMap<>();

		for (String word : strs) {
			char[] chars = word.toCharArray();
			Arrays.sort(chars);
			String sortedWord = new String(chars);

			if (!map.containsKey(sortedWord)) {
				map.put(sortedWord, new ArrayList<>());
			}

			map.get(sortedWord).add(word);
		}

		return new ArrayList<>(map.values());
	}

	public static void main(String args[]) {
		System.out.println(groupAnagrams(new String[] { "eat", "tea", "tan", "ate", "nat", "bat" }));
	}

}
