package twoPointer;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

//this ques is similar to PermutationInString
public class _0014_FindAllAnagramsInAString {

//	time complexity - O(alphabet size * length(s))

	public List<Integer> findAnagrams(String s, String p) {
		List<Integer> ans = new ArrayList<>();
		int[] hash = new int[26];
		int[] phash = new int[26];
		int window = p.length();
		int len = s.length();

		if (len < window) {
			return ans;
		}

		int left = 0;
		int right = 0;

		while (right < window) {
			phash[p.charAt(right) - 'a']++;
			hash[s.charAt(right) - 'a']++;
			right++;
		}
		right--;

		while (right < len) {
			if (Arrays.equals(phash, hash)) {
				ans.add(left);
			}
			right++;
			if (right != len) {
				hash[s.charAt(right) - 'a']++;
			}
			hash[s.charAt(left) - 'a']--;
			left++;
		}

		return ans;
	}
}
