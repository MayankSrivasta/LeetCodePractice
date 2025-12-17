package _0002_TwoPointerSlidingWindow;

public class _0020_RemoveDuplicatesFromSortedArray2 {
	
	
	
	public int removeDuplicates(int[] nums) {

		int i = 0;
		for (int j = 0; j < nums.length; j++) {
			if (i < 2 || nums[i - 2] != nums[j]) {
				nums[i++] = nums[j];
			}
		}
		return i;
	}
	
}
