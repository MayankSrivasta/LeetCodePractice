package _0001_ArrayAndHashing;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

// its premium question on leetcode so not available, its only available on NeetCode.io
//https://neetcode.io/problems/string-encode-and-decode

//completed this question on NeetCode.io website directly
public class _0005_EncodeDecodeStrings {

	public static String encode(List<String> strs) {
		StringBuilder encodedString = new StringBuilder();
		for (String str : strs) {
			encodedString.append(str.length()).append("#").append(str);
		}
		return encodedString.toString();
	}

//	ENCODE 4#neet 4#code 4#love3#you
//	DECODE [neet, code, love, you]

	public static List<String> decode(String str) {
		List<String> list = new ArrayList<>();
		int i = 0;
		while (i < str.length()) {
			int j = i;

			while (str.charAt(j) != '#')
				j++;

//			this returns the index of integer value for for the length of the word
//			this substring is required because in-case if it returns 2-digit no. then it will fail using charAt() 			
			int length = Integer.valueOf(str.substring(i, j));

//			this gives the end index of the word to create a substring
			i = j + 1 + length;
			list.add(str.substring(j + 1, i));
		}
		return list;
	}

	public static void main(String args[]) {
//		ENCODE 4#neet 4#code 4#love3#you
//		DECODE [neet, code, love, you]
//		System.out.println("ENCODE" + encode(new ArrayList<>(Arrays.asList("we", "say", ":", "yes", "!@#$%^&*()"))));
		System.out.println(
				"DECODE " + decode(encode(new ArrayList<>(Arrays.asList("we", "say", ":", "yes", "!@#$%^&*()")))));
	}

}
