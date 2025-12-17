package _0002_TwoPointerSlidingWindow;

public class _0003_MaximumPointsYouCanObtainFromCards {

	
//	cardPoints = [1,2,3,4,5,6,1], k = 3
//	its simple one only, u just need to draw the diagram of it to understand the approach
	public static int maxScore3(int[] cardPoints, int k) {
		int lsum = 0;
		for (int i = 0; i < k; i++)
			lsum += cardPoints[i];
		int sum = lsum;
		int j = cardPoints.length - 1;
		int rsum = 0;
		for (int i = k - 1; i >= 0; i--) {
			lsum -= cardPoints[i];
			rsum += cardPoints[j];
			j--;

			sum = Math.max(sum, lsum + rsum);
		}
		return sum;
	}
	
	

//	APPROACH - 2
//	TRY TO UNDERSTAND THIS APPROACH ITS THE SAME APPROACH GIVEN BY NEETCODE
//	https://www.youtube.com/watch?v=TsA4vbtfCvo
	public int maxScore2(int[] cardPoints, int k) {
		int len = cardPoints.length;
		int l = 0, r = len - k;
		int total = 0;
		for (int i = r; i < len; i++)
			total += cardPoints[i];
		int res = total;
		while (r < len) {
			total += (cardPoints[l] - cardPoints[r]);
			res = Math.max(res, total);
			l++;
			r++;
		}
		return res;
	}

//	APPROACH - 1
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

//							0 1 2 3 4 5 6	
//							1,2,3,4,5,6,1

//						    7 - 3 - 1 = 3

		for (int i = 0; i < n - k - 1; i++) {
//			1 + 2 + 3 = 6
			window += cards[i];
		}

//		starting from 4 then 5,6,1
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
//		7 elements
		maxScore3(new int[] { 1, 2, 3, 4, 5, 6, 1 }, 3);
	}

}
