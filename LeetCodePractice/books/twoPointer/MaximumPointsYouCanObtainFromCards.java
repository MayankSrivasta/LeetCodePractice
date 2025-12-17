package twoPointer;

public class MaximumPointsYouCanObtainFromCards {

	public static int maxScore(int[] cards, int k) {
		int n = cards.length;
		int sum = 0;
		int max = 0;
		for (int i = 0; i < n; i++) {
			sum += cards[i];
		}
		if (n == k)
			return sum;
		int window = 0;
		for (int i = 0; i < n - k - 1; i++) {
			window += cards[i];
		}
		for (int i = n - k - 1; i < n; i++) {
			window += cards[i];
			max = Math.max(max, sum - window);
			
//			not able to understand below line of code properly
			window -= cards[i - (n - k - 1)];
		}
		return max;
	}

	public static void main(String args[]) {
		maxScore(new int[]{1,2,3,4,5,6,1}, 3);
	}

}
