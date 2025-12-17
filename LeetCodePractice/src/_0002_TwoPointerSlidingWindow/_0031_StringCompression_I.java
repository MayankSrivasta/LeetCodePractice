package _0002_TwoPointerSlidingWindow;

public class _0031_StringCompression_I {

//	kevin naughton junior youtube
	public static int compress(char[] chars) {
		int index = 0;
		int i = 0;
		while (i < chars.length) {
			int j = i;
			while (j < chars.length && chars[j] == chars[i]) {
				j++;
			}
			chars[index++] = chars[i];
			if (j - i > 1) {
				String count = (j - i) + "";
//				this for loop is used in case if 2 digit number is coming like 12, 15,
//				then it needs to be looped.
//				it also needs to be looped because chars[] is an char array & for each array element
//				the values needs to be put in.
				for (char c : count.toCharArray()) {
					chars[index++] = c;
				}
			}
			i = j;
		}
		return index;
	}

//		ayushi sharma youtube
	public int compress2(char[] chars) {
		int i = 0;
		int count = 1;
		for (int j = 1; j <= chars.length; j++, count++) {
			if (j == chars.length || chars[j] != chars[j - 1]) {
				chars[i++] = chars[j - 1];
				if (count >= 2) {
					String countStr = Integer.toString(count);
					for (char digit : countStr.toCharArray()) {
						chars[i++] = digit;
					}
				}
				count = 0;
			}
		}
		return i;
	}

	public static void main(String args[]) {
		System.out.println(compress(new char[] { 'a', 'a', 'b', 'b', 'c', 'c', 'c' }));
	}

}
