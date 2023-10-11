package leetCode;

import java.util.HashMap;

public class TwoSum {

	static int i = 5;

	public static void main(String args[]) 
	{

		twoSum(new int[] {2, 7, 11, 15}, 9);
		
	}

	public static int[] twoSum(int[] nums, int target) {

		HashMap<Integer, Integer> hm = new HashMap<>();

		for (int i = 0; i < nums.length; i++) {
			int k = target - nums[i];
			if (!hm.containsKey(k))
				hm.put(nums[i], i);
			else
				return new int[] { hm.get(k), i };
		}
		return new int[] { -1, -1 };
	}

}
