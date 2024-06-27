package stringQues;

import java.util.HashMap;

public class stringQues {

//	public static void main(String[] args) {
//		int arr[] = new int[] { 5, 4, 3, 2, 1 };
//
//		boolean isVisited[] = new boolean[arr.length + 1];
//
//		HashMap<Integer, Integer> nodeMap = new HashMap<Integer, Integer>();
//
//		for (int i = 1; i < isVisited.length; i++) {
//			nodeMap.put(i, arr[i - 1]);
//		}
//		int countSwap = 0;
//
//		for (int k = 1; k <= nodeMap.size(); k++) {
//
//			int nextNode;
//
//			if (isVisited[k] == false) {
//				isVisited[k] = true;
//
//				if (k == nodeMap.get(k)) {
//					continue;
//				} else {
//					int c = nodeMap.get(k);
//					while (!isVisited[c]) {
//
//						isVisited[c] = true;
//
//						nextNode = nodeMap.get(c);
//						c = nextNode;
//						++countSwap;
//					}
//				}
//			}
//		}
//
//		System.out.println("swap count :" + countSwap);
//	}
}