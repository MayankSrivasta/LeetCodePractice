package practice;

import java.util.Scanner;

public class Chalk {

	public static void main(String args[]) {
		float n, root, count = (float) 0.00;

		int val = 1, days, ans;

		System.out.println("enter");
		Scanner input = new Scanner(System.in);
		n = input.nextFloat();

		root = (float) (1 / Math.sqrt(n));

		for (int i = 0; i < n; i++)

			count = root + count;

		days = (int) (count);

		ans = (int) (n + days);

		System.out.println(ans + 1);
	}
}
