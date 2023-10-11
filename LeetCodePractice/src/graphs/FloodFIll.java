package graphs;

public class FloodFIll {
	class Solution {
		public int[][] floodFill(int[][] image, int i, int j, int newColor) {
			int oldColor = image[i][j];
			if (image[i][j] != newColor)
				dfsFill(image, i, j, oldColor, newColor);

			return image;
		}

		void dfsFill(int[][] image, int i, int j, int oldColor, int newColor) {
			if (i >= 0 && j >= 0 && i < image.length && j < image[0].length && image[i][j] == oldColor) {
				image[i][j] = newColor;
				dfsFill(image, i - 1, j, oldColor, newColor);
				dfsFill(image, i + 1, j, oldColor, newColor);
				dfsFill(image, i, j - 1, oldColor, newColor);
				dfsFill(image, i, j + 1, oldColor, newColor);

			}
		}
	}

}
