package _0001_ArrayAndHashing;

import java.util.ArrayList;
import java.util.List;

public class _0003_SummaryRanges {

//	https://www.youtube.com/watch?v=ZHJDwbfqoa8
	public List<String> summaryRanges(int[] nums) {
		List<String> ans = new ArrayList<>();
		int n = nums.length;
		int i = 0;
		int j = 0;

		while (j < n) {
			int start = nums[i];
//			here its checking [i < n - 1] for overcoming the segmentation fault in the 2nd condition
//			& there is no break in between the given numbers, then i just keeps on incrementing
			while (i < n - 1 && nums[i] + 1 == nums[i + 1]) {
				i++;
			}
//			if the start & end nos are different, it will happen like 1 -> 3, then will add start & end nos.
			if (start != nums[i]) {
				ans.add(start + "->" + nums[i]);
			} else {
//				else if its a single no. then add that single number without any arrow symbols
				ans.add(String.valueOf(nums[i]));
			}
			i++;
		}

		return ans;
	}
}
