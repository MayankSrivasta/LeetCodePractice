package _0001_ArrayAndHashing;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class _0018_FindAllDisappearedInAnArray {
	// Since the array has values form 0 to n we can use in-place sorting that's
	// O(N) time and constant space.

	public List<Integer> findDisappearedNumbers(int[] nums) {
		Set<Integer> numSet = new HashSet<>();
		List<Integer> missingNumbers = new ArrayList<>();

		// Add all numbers in the set
		for (int num : nums) {
			numSet.add(num);
		}

		// Find the missing numbers
		for (int i = 1; i <= nums.length; i++) {
			if (!numSet.contains(i)) {
				missingNumbers.add(i);
			}
		}

		return missingNumbers;
	}

}
