package twoPointer;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class OceanView {

	public static int[] findBuildings2(int[] heights) {
		int n = heights.length;
		List<Integer> list = new ArrayList<>();
		int maxHeight = -1;

		for (int current = n - 1; current >= 0; --current) {

			if (maxHeight < heights[current]) {
				list.add(current);
				maxHeight = heights[current];
			}
		}

//		below line is just converting list to an array
		return list.stream().mapToInt(i -> i).toArray();

//		below 3 lines are just converting list to an array
//		int[] answer = new int[list.size()];
//		for (int i = 0; i < list.size(); ++i) {
//			answer[i] = list.get(list.size() - 1 - i);
//		}
//		return answer;
	}

	public int[] findBuildings(int[] heights) {
		int mx = 0;
		LinkedList<Integer> ans = new LinkedList<>();

		for (int i = heights.length - 1; i >= 0; --i) {
			int v = heights[i];
			if (mx < v) {
				ans.addFirst(i);
				mx = v;
			}
		}
		return ans.stream().mapToInt(i -> i).toArray();
	}

}
