package _0002_TwoPointerSlidingWindow;

public class _0024_SortColors {

//	AYUSHI SHARMA YOUTUBE SOLUTION
//	https://www.youtube.com/watch?v=Kov-M_lTuOA
	
//	since this question needs to be done in O(n), time that's why this approach is being used here
//	no need to put lot of brain in this question just an intuitive approach is required
	
	void sortColors(int nums[]) {
		int n = nums.length;
		int i = 0, j = n - 1, curr = 0;

		while (curr <= j) {
			if (nums[curr] == 2) {
				swap(nums, curr, j);
				j--;
			} else if (nums[curr] == 1) {
				curr++;
			} else {
				swap(nums, curr, i);
				i++;
				curr++;
			}
		}
	}

	void swap(int[] nums, int p1, int p2) {
		int temp = nums[p1];
		nums[p1] = nums[p2];
		nums[p2] = temp;
	}
}
 