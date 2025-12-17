package _0001_ArrayAndHashing;

public class _0009_LongestCommonPrefix {

//	solution from NeetCode
//	 strs = ["flower","flow","flight"]
	public static String longestCommonPrefix(String[] strs) {
		StringBuilder res = new StringBuilder();

		for (int i = 0; i < strs[0].length(); i++) {
			for (String s : strs)
				if (i == s.length() || s.charAt(i) != strs[0].charAt(i))
					return res.toString();
			res.append(strs[0].charAt(i));
		}
		return res.toString();
	}

//	old submission
	public static String longestCommonPrefix2(String[] strs) {
		if (strs == null || strs.length == 0)
			return "";
		String ans = strs[0];
		for (int i = 0; i < strs[0].length(); i++) {
			char ch = ans.charAt(i);
			for (int j = 1; j < strs.length; j++) {
				if (i >= strs[j].length() || ch != strs[j].charAt(i))
					return ans.substring(0, i);
			}
		}

		return ans;
	}

	public static void main(String args[]) {
//		System.out.println(longestCommonPrefix2(new String[] { "flower", "flow", "flight" }));
		System.out.println(longestCommonPrefix2(new String[] { "" }));

	}

}
