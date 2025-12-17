package _0001_ArrayAndHashing;

public class _0008_LengthOfLastWord {

	public static int lengthOfLastWord(String s) {

		int i = s.length() - 1, length = 0;
		
//		its work is to only remove ' ' from the reverse of the given string
		while (s.charAt(i) == ' ') {
			i -= 1;
		}
//		once all the empty space is removed from the reverse of the string then
//		calculate the length of the string & also keep on decrementing the value of i.
		while (i >= 0 && s.charAt(i) != ' ') {
			length += 1;
			i -= 1;
		}
		return length;
	}

	public static void main(String args[]) {
		System.out.println(lengthOfLastWord("Hello World"));
	}
}
