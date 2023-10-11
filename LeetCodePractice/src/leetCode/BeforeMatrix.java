package leetCode;

import java.util.ArrayList;
import java.util.List;

public class BeforeMatrix {

	public static void main(String args[]) {

		List<List<Integer>> list = new ArrayList();
		
		list.add(new ArrayList());
		list.add(new ArrayList());
		list.get(0).add(2);
		list.get(0).add(5);
		list.get(1).add(7);
		list.get(1).add(17);
		
//		findnewArrMatrix(list).stream().forEach(System.out::println);;
		
		
	}

	static List<List<Integer>> findBeforeMatrix(List<List<Integer>> before) {
		int n = before.size();
		int m = before.get(0).size();
		int arr[][] = new int[n][m];

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				arr[i][j] = before.get(i).get(j);
			}
		}

		int newArr[][] = new int[n][m];

		int s = arr[0][0];

		for (int i = 1; i < n; i++) {
			newArr[i][0] = (arr[i][0] - s);
			s += newArr[i][0];
		}
		s = arr[0][0];
		newArr[0][0] = arr[0][0];
		for (int i = 1; i < m; i++) {
			newArr[0][i] = (arr[0][i] - s);
			s += newArr[0][i];
		}
		for (int i = 1; i < n; i++) {
			for (int j = 1; j < m; j++) {
				newArr[i][j] = arr[i][j] - (newArr[i - 1][j] + newArr[i][j - 1] + newArr[i - 1][j - 1]);
			}
		}

		List<List<Integer>> list = new ArrayList<List<Integer>>();
		
		for(int i = 0; i < m; i++)
			list.add(new ArrayList());
		
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				list.get(i).add(newArr[i][j]);
			}
		}

		return list;
	}

}
