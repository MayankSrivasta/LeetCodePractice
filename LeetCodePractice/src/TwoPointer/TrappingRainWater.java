package TwoPointer;

public class TrappingRainWater {

	public int trap(int[] height) {

		int length = height.length;
		int left[] = new int[length];
		int right[] = new int[length];

		for (int i = 1; i < length; i++) {
			left[i] = Math.min(left[i - 1], right[length - i]);
			right[length - i - 1] = Math.min(left, 0);
		}

		return 0;
	}

}
