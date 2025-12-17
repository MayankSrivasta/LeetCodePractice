package _0001_ArrayAndHashing;

public class _0016_FindPivotIndex {

//	nums = [1,7,3,6,5,6]
	
	public int pivotIndex(int[] nums) {
		int totalSum = 0;
		for (int i = 0; i < nums.length; i++) {
			totalSum += nums[i];
		}
		int leftSum = 0;
		for (int i = 0; i < nums.length; i++) {
			int rightSum = totalSum - leftSum - nums[i];
			if (leftSum == rightSum) {
				return i;
			}
			leftSum += nums[i];
		}
		return -1;
	}
}
