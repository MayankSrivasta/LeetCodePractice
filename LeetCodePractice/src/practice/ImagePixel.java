package practice;

public class ImagePixel {

	public static void main(String args[]) {
		int m = 3, n = 3;
		int arr[][] = new int[m][n];

	}

	int[][] t(int arr[][], int m, int n) {

		int returnArr[][] = new int[m][n];

		int i = 0, j = 0;
		while (i < m && j < n) {
			int blackCount = 0;
			int whiteCount = 0;
			for (int k = i; k < m; k++) {
				if (arr[k][j] == 1)
					blackCount++;
				else
					whiteCount++;
			}

			for (int l = j; l < n; l++) {
				if (arr[i][l] == 1)
					blackCount++;
				else
					whiteCount++;
			}

			int diff = blackCount - whiteCount;

			for (int k = i; k < m; k++) {
				if (arr[k][j] == 1)
					arr[k][j] = diff;

			}

			for (int l = j; l < n; l++) {
				if (arr[i][l] == 1)
					arr[i][l] = diff;

			}

			i++;
			j++;
		}

		return returnArr;

	}

}
