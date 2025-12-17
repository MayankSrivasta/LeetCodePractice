package _0001_ArrayAndHashing;

import java.util.ArrayList;
import java.util.List;

public class _0010_PascalsTriangle {

	public static List<List<Integer>> generate(int numRows) {

		List<List<Integer>> res = new ArrayList<>();

		for (int i = 0; i < numRows; i++) {
			List<Integer> list = new ArrayList<>();
			for (int j = 0; j <= i; j++) {
//				this 'if' condition will only satisfy for adding up nos. like 2, 3, 4 in the given
//				image on the LC side, else it will just keep on adding '1'.

//				The condition mainList.get(i - 1).size() - 1 >= j ensures that:
//
//					Position Validity: When calculating the value for list.get(j), 
//					you need to ensure that the indices j - 1 and j in the previous row (i - 1) are valid. 
//					That means j should not exceed the number of elements in the previous row.

//				i = 2, j = 1
//				since in below size() is written that's why (-1) is included here,
//				because size will give length=2 but the actual index value will be 1

				if (j > 0 && i > 0 && res.get(i - 1).size() - 1 >= j) {
					list.add(res.get(i - 1).get(j - 1) + res.get(i - 1).get(j));
				} else {
					list.add(1);
				}
			}
			res.add(list);
		}

		return res;

	}

	public static void main(String args[]) {
		System.out.println(generate(5));
	}
}
