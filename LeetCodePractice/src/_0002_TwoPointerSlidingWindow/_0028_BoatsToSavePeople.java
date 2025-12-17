package _0002_TwoPointerSlidingWindow;

public class _0028_BoatsToSavePeople {

//	https://leetcode.com/problems/boats-to-save-people/description/

//	https://www.youtube.com/watch?v=GqT3BFKdh-I

	public int numRescueBoats(int[] people, int limit) {

		// Arrays.sort(people);

//		from here 1 to 2, is count sort algorithm used, either u can use above sorting approach
//		or use below count sorting which will reduce the complexity to O(N) or in-case using given sorting algorithm
//		then in this case the complexity will be O(NlogN)
//		--> 1
		int[] count = new int[limit + 1];
		for (int p : people) {
			count[p]++;
		}

		int index = 0;
		for (int val = 1; val <= limit; val++) {
			while (count[val]-- > 0) {
				people[index++] = val;
			}
		}

//		--> 2

		int left = 0, right = people.length - 1;
		int boats = 0;
		while (left <= right) {
			if (people[left] + people[right] <= limit) {
				left++;
				right--;
			} else {
				right--;
			}
			boats++;
		}
		return boats;
	}

}
