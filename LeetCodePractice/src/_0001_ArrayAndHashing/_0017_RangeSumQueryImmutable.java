package _0001_ArrayAndHashing;

public class _0017_RangeSumQueryImmutable {

	public int[] arr;

//	Constructor
//	PREFIX SUM
//	[-2, 0, 3, -5, 2, -1]
//	[-2, -2, 1, -4,-2, -3]
	public _0017_RangeSumQueryImmutable(int[] nums) {
//		arr = nums;
		arr = new int[nums.length];
		arr[0] = nums[0];
		for (int i = 1; i < arr.length; i++) {
			arr[i] += arr[i - 1];
		}
	}

	public int sumRange(int left, int right) {
		if (left == 0) {
			return arr[right];
		}
		return arr[right] - arr[left - 1];
	}

	public static void main(String args[]) {
		_0017_RangeSumQueryImmutable obj = new _0017_RangeSumQueryImmutable(new int[] { -2, 0, 3, -5, 2, -1 });
		System.out.println(obj.sumRange(0, 2));

	}
}

/**
 * Your NumArray object will be instantiated and called as such: NumArray obj =
 * new NumArray(nums); int param_1 = obj.sumRange(left,right);
 */