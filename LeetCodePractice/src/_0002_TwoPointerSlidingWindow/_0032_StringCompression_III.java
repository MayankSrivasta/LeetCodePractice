package _0002_TwoPointerSlidingWindow;

public class _0032_StringCompression_III {

	public String compressedString(String word) {
//		easy question only
		int n = word.length();
		int count = 0;
		int i = 0;
		int j = 0;
		StringBuilder ans = new StringBuilder();

		while (j < n) {
			count = 0;
			while (j < n && word.charAt(i) == word.charAt(j) && count < 9) {
				j++;
				count++;
			}
			ans.append(count).append(word.charAt(i));
			i = j;
		}

		return ans.toString();
	}
}
