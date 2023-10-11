package leetCode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Sum3 {

	public static List<List<Integer>> threeSum(int[] nums) {
		Arrays.sort(nums);
		List<List<Integer>> res = new ArrayList<>();
		for (int i = 0; i < nums.length && nums[i] <= 0; ++i)
			if (i == 0 || nums[i - 1] != nums[i]) {
				twoSumII(nums, i, res);
			}
		return res;
	}

	static void twoSumII(int[] nums, int i, List<List<Integer>> res) 
	{
		int lo = i + 1, hi = nums.length - 1;
		while (lo < hi) {
			int sum = nums[i] + nums[lo] + nums[hi];
			if (sum < 0) {
				++lo;
			} else if (sum > 0) {
				--hi;
			} else {
				res.add(Arrays.asList(nums[i], nums[lo++], nums[hi--]));
//				nums[lo] == nums[lo - 1] this line is checking that the adjacent nos. are not duplicate
				while (lo < hi && nums[lo] == nums[lo - 1])
					++lo;
			}
		}
	}
	
	public static void main(String args[])
	{
		System.out.println(threeSum(new int[] {-1,0,1,2,-1,-4}));
	}

}
