package _0005_BinarySearch;

public class _0001_BinarySearch {

	
//	Input: nums = [-1,0,2,4,6,8], target = 4
//					0,1,2,3,4,5 
	public int search(int[] nums, int target) {
		int l = 0, r = nums.length - 1;

		while (l <= r) {
			int m = l + ((r - l) / 2);
			if (nums[m] > target) {
				r = m - 1;
			} else if (nums[m] < target) {
				l = m + 1;
			} else {
				return m;
			}
		}
		return -1;
	}
}
