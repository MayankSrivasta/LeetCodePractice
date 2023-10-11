package leetCode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;

public class CardinallitySorting {

	public static void main(String args[]) {

		List<Integer> s = new ArrayList<Integer>();
		s.add(31);
		s.add(15);
		s.add(7);
		s.add(3);
		s.add(2);
		
		
		List<Integer> list = cardinalitySort(s);
		
		list.stream().forEach(System.out::println);
		
	}

	public static int[] sortByBits(int[] arr) {
		var nums = Arrays.stream(arr).boxed().toArray(Integer[]::new);

		Arrays.sort(nums, Comparator.comparingInt(Integer::bitCount).thenComparingInt(n -> n));

		return Arrays.stream(nums).mapToInt(Integer::intValue).toArray();
	}

	public static List<Integer> cardinalitySort(List<Integer> nums) {

		int[] arr = new int[nums.size()];

		for (int i = 0; i < nums.size(); i++) {
			arr[i] = nums.get(i);
		}

		var numbs = Arrays.stream(arr).boxed().toArray(Integer[]::new);

		Arrays.sort(numbs, Comparator.comparingInt(Integer::bitCount).thenComparingInt(n -> n));

		int returnArr[] = Arrays.stream(numbs).mapToInt(Integer::intValue).toArray();

		List<Integer> list = new ArrayList();
		for (int i = 0; i < returnArr.length; i++) {
			list.add(returnArr[i]);
		}

		return list;

	}

}
