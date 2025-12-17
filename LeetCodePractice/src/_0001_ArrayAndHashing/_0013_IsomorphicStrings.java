package _0001_ArrayAndHashing;

import java.util.HashMap;

public class _0013_IsomorphicStrings {

	
   	public static boolean isIsomorphic3(String s, String t) {

		int map1[] = new int[128];
		int map2[] = new int[128];

		if (s.length() != t.length())
			return false;

		for (int i = 0; i < s.length(); i++) {
			char sCh = s.charAt(i);
			char tCh = t.charAt(i);
         int sMap1 = map1[sCh];
         int tMap1 = map2[tCh];
 			if (sMap1 != tMap1)
				return false;

			map1[s.charAt(i)]++;
			map2[t.charAt(i)]++;
		}
		return true;
	}

	
	
	
	public static boolean isIsomorphic(String s, String t) {

		int map1[] = new int[128];
		int map2[] = new int[128];

		if (s.length() != t.length())
			return false;

		for (int i = 0; i < s.length(); i++) {
			char sCh = s.charAt(i);
			char tCh = t.charAt(i);
			if (map1[sCh] != map2[tCh])
				return false;

			map1[s.charAt(i)] = i + 1;
			map2[t.charAt(i)] = i + 1;
		}
		return true;
	}

//	using hashmap we are just checking whether the mappings are correct or not as given in neetcode video
	public static boolean isIsomorphic2(String s, String t) {
		HashMap<Character, Character> mapS = new HashMap<>();
		HashMap<Character, Character> mapT = new HashMap<>();

		int s1 = 0, t1 = 0;

		while (s1 < s.length() && t1 < t.length()) {
//			in this if condition we are just checking whether the mapping are correct or not
			if ((mapS.containsKey(s.charAt(s1)) && mapS.get(s.charAt(s1)) != t.charAt(t1))
					|| 
				(mapT.containsKey(t.charAt(t1)) && mapT.get(t.charAt(t1)) != s.charAt(s1))) {
				return false;
			}
//			here we are creating the mapping & in the above code we are just checking whether the mapping 
//			are correct or not
			mapS.put(s.charAt(s1), t.charAt(t1));
			mapT.put(t.charAt(t1), s.charAt(s1));
			s1 += 1;
			t1 += 1;
		}
		return true;
	}

	public static void main(String args[]) {
		System.out.println(isIsomorphic3(new String("bbbaaaba"), new String("aaabbbba")));
	}
}
