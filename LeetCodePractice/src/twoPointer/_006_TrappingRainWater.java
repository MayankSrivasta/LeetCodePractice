package twoPointer;

//question type - hard
public class _006_TrappingRainWater {

//	solution from LeetCode
	public int trap(int[] height) {
		int left = 0, right = height.length - 1, leftMax = 0, rightMax = 0, water = 0;

		while (left < right) {
			if (height[left] < height[right]) {
				if (leftMax < height[left])
					leftMax = height[left];
				else
					water += leftMax - height[left];
				left++;

			} else {
				if (rightMax < height[right])
					rightMax = height[right];
				else
					water += rightMax - height[right];
				right--;
			}
		}
		return water;
	}

//	THIS ONE IS EASIER TO UNDERSTAND
	public static int trap2(int[] height) {

		int n = height.length;
		if (n <= 2)
			return 0;

//		created 2 array, one from left & one from right side
//		finding max height from left side & then max height from right side 
		int left[] = new int[n], right[] = new int[n];
		left[0] = height[0];
		right[n - 1] = height[n - 1];

		for (int i = 1; i < n; i++) {
			left[i] = Math.max(left[i - 1], height[i]);
			right[n - i - 1] = Math.max(right[n - i], height[n - i - 1]);
		}

		int water = 0;
		for (int i = 0; i < n; i++) {
			water += Math.min(left[i], right[i]) - height[i];
		}
		return water;
	}

	public static void main(String args[]) {
		System.out.println(trap2(new int[] { 7, 0, 4, 2, 5, 0, 6, 4, 0, 5 }));
	}

}
