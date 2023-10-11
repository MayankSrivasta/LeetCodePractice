package leetCode;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Tour {

	public static void main(String[] args) {

		List<Integer> list = new ArrayList();
		list.add(5);
		list.add(4);
		list.add(3);
		list.add(2);
		list.add(1);

		least_expendature(list);

	}

	public static void least_expendature(List<Integer> options) {
		Collections.sort(options);
		int arr[] = new int[2];

		for (int i = 0; i < 2; i++)
			arr[i] = options.get(i);

		options = new ArrayList();

		for (int i = 0; i < arr.length; i++)
			options.add(arr[i]);

		for (int a : options)
			System.out.println(a);
	}

}
