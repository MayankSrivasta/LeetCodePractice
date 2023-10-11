package leetCode;

public class SumEvens {

	public static void main(String args[]) {

		System.out.println(solution(10));

	}

	public static long solution(long n) {
		long sum = 0;
		for (long i = 0; i <= n; i++) {
			if (i % 2 == 0) {
				sum += i;
			}
		}
		return sum;
	}
}