package twoPointerSlidingWindow;

public class _0005_ContainerWithMostWater {

	
//	brute force approach
	public static int maxArea2(int[] a) {

		int Area = 0;

		for (int i = 0; i < a.length; i++) {
			for (int j = i + 1; j < a.length; j++) 
			{
				Area = Math.max(Area, Math.min(a[i], a[j]) * (j - i));
			}
		}
		return Area;
	}

	
//	optimal solution
	public int maxArea(int[] height) {
		int left = 0, right = height.length - 1, max = 0;
		while (left < right) {
			if (height[left] < height[right]) {
				max = Math.max(max, height[left] * (right - left));
				left++;
			} else {
				max = Math.max(max, height[right] * (right - left));
				right--;
			}
		}
		return max;
	}


}
