package _0001_ArrayAndHashing;

import java.util.HashSet;
import java.util.Set;

public class _0012_UniqueEmailAddress {

	private static String getFormattedEmail(String email) {
		String[] arr = email.split("@");
		String localName = arr[0];
		String domainName = arr[1];

		// Only keep the first part of "+" sign
		String[] arrLocalWithPlus = localName.split("\\+");
		localName = arrLocalWithPlus[0];

		// Replace "."/dots
		localName = localName.replace(".", "");

		return localName + "@" + domainName;
	}

	public static int numUniqueEmails(String[] emails) {
		Set<String> uniqueEmails = new HashSet<>();
		for (String email : emails) {
			String formattedEmail = getFormattedEmail(email);
			uniqueEmails.add(formattedEmail);
		}
		return uniqueEmails.size();
	}

	public static void main(String args[]) {

		System.out.println(numUniqueEmails(new String[] { "test.email+alex@leetcode.com",
				"test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com" }));

	}
}
