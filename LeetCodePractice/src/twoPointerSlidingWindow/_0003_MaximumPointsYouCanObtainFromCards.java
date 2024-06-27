package twoPointerSlidingWindow;

public class _0003_MaximumPointsYouCanObtainFromCards {

	
//	difficult question
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
//			check if below code can be written using 2 pointer, adding one more variable
//			left variable to maintain left pointer for decrementing the value
//			of the sliding window from left side.
			window -= cards[i - (n - k - 1)];
		}
		return max;
	}

	public static void main(String args[]) {
		maxScore(new int[]{1,2,3,4,5,6,1}, 3);
	}

}
