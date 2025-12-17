package _0002_TwoPointerSlidingWindow;

public class _0017_MoveZeroes {
	
//	https://leetcode.com/problems/move-zeroes/description/?source=submission-ac
	public void moveZeroes(int[] nums) {
		int left = 0;

//		Input: nums = [0,1,0,3,12]
//		Output:       [1,3,12,0,0]
		
		
		for (int right = 0; right < nums.length; right++) {
			if (nums[right] != 0) {
				int temp = nums[right];
				nums[right] = nums[left];
				nums[left] = temp;
				left++;
			}
		}
	}
}
