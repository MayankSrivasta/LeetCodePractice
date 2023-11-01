package twoPointer;

public class _009_LongestCommonPrefix {

//	Question/Answer Video link
//	https://www.udemy.com/course/coding-interview-question-data-structures-algorithm/learn/lecture/17909208#overview

	public String longestCommonPrefix(String[] strs) {
		if (strs == null || strs.length == 0)
			return "";

		String ans = strs[0];

		for (int i = 0; i < ans.length(); i++) {
			char currentChar = ans.charAt(i);

			for (int j = 1; j < strs.length; j++) {
//				below first condition is written to stop from segmentation fault in 2nd condition.
				if (i >= strs[j].length() || currentChar != strs[j].charAt(i)) {
					return ans.substring(0, i);
				}
			}
		}

		return ans;
	}

}
