package leetCode;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Reverse {

	public static void main(String args[]) 
	{

		List<Integer> arr = new ArrayList<>();
		arr.add(3);
		arr.add(1);
		arr.add(2);
		arr.add(3);
		arr.add(3);
		arr.add(2);
		
		List<List<Integer>> arr2 = new ArrayList<>();
		List<Integer> arr3 = new ArrayList<>();
		
		arr3.add(0);
		arr3.add(2);
		
		List<Integer> arr4 = new ArrayList<>();
		arr4.add(1);
		arr4.add(2);
		
		List<Integer> arr5 = new ArrayList<>();
		arr5.add(0);
		arr5.add(2);
		
		arr2.add(arr3);
		arr2.add(arr4);
		arr2.add(arr5);
		
		System.out.println(performOperations(arr, arr2));
	}

	public static List<Integer> performOperations(List<Integer> arr, List<List<Integer>> operations) {

		for( List<Integer> op : operations)
		{
			int a = op.get(0);
			int b = op.get(1);
	
			
			int l = Math.min(a, b);
	        int r = Math.max(a, b);
	        List<Integer> list = arr.subList(l, r + 1);
	        
	        Collections.sort(list);
	        
		}
        
		return arr;
		
	}

}
