package _0001_ArrayAndHashing;

public class _0011_RemoveElements {

	public int removeElement(int[] nums, int val) {

		int i = 0, j = 0;

		for (j = 0; j < nums.length; j++) {
			if (nums[j] != val)
				nums[i++] = nums[j];
		}
		return i;
	}
}