package twoPointer;

public class _5_ContainerWithMostWater 
{

	public int maxArea(int[] height) 
	{
		int left = 0, right = height.length - 1, max = 0;
		while (left < right) 
		{
			if (height[left] < height[right]) 
			{
				max = Math.max(max, height[left] * (right - left));
				left++;
			}
			else 
			{
				max = Math.max(max, height[right] * (right - left));
				right--;
			}
		}
		return max;
	}
	
}
