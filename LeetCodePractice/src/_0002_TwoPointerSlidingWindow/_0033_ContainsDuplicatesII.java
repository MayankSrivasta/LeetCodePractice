package _0002_TwoPointerSlidingWindow;

import java.util.HashSet;
import java.util.Set;

public class _0033_ContainsDuplicatesII {

	public static boolean containsNearbyDuplicate(int[] nums, int k) {
		Set<Integer> window = new HashSet<>();
		int left = 0;
		for (int right = 0; right < nums.length; right++) {

			if (window.size() > k) {
				window.remove(nums[left]);
				left++;
			}

			if (window.contains(nums[right])) {
				return true;
			}

			window.add(nums[right]);
		}

		return false;
	}

	public static void main(String args[]) {
		System.out.println(containsNearbyDuplicate(new int[] { 1, 2, 3, 4, 5, 1 }, 3));
	}
}