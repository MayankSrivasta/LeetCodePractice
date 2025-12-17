package _0002_TwoPointerSlidingWindow;

import java.util.ArrayDeque;
import java.util.Deque;
import java.util.LinkedList;

public class _0029_SlidingWindowMaximum {

//	https://www.youtube.com/watch?v=DfljaUwZsOk

//	this solution is taken from NeedCode.io git repo
	public static int[] maxSlidingWindow(int[] nums, int k) {
		if (nums == null || nums.length == 0)
			return new int[0];

		int n = nums.length;

//			i - k + 1 -->> this maintains the window size
//	        resulting window size
		int[] res = new int[n - k + 1];
		Deque<Integer> deque = new LinkedList<>();

		for (int i = 0; i < n; i++) {

			// Remove elements from deque smaller than current element
			while (!deque.isEmpty() && nums[deque.peekLast()] < nums[i]) {
//	            	removes element from the end of the dequeue
				deque.pollLast();
			}

			// Add current element at the end of the deque
			deque.offer(i);

			// Remove elements not in the sliding window
//        	it is used to maintain the size of the window by removing the elements from the DEQUE front
//        	here (i - k + 1) represents the initial pointer of the window
			if (!deque.isEmpty() && deque.peek() < i - k + 1) {
//            	removes element from the front
				deque.poll();
			}

			// The first element in deque is the maximum element in the current window
//	            this will only start operating once it reaches the threshold of k,
//	            it will automatically start setting the first element from the queue to output,
//	            considering that the first element maximum.
//	            it is only used to maintain the size of the window & set the element on the front 
//	            of the deque to the output
//	            once the value of i reaches the threshold value(K) it will automatically starts
//	            popping out the front elements from the queue to the output
			if (i >= k - 1) {
				res[i - k + 1] = nums[deque.peek()];
			}
		}

		return res;
	}

//	https://www.youtube.com/watch?v=ZiZWg0gjJhE
//	Engineering Digest youtube
	public static int[] maxSlidingWindow2(int[] nums, int k) {
		int res[] = new int[nums.length - k + 1];
		int j = 0;

		ArrayDeque<Integer> queue = new ArrayDeque();

		for (int i = 0; i < nums.length; i++) {

			while (!queue.isEmpty() && nums[queue.getLast()] < nums[i]) {
				queue.removeLast();
			}

			queue.addLast(i);

			if (queue.getFirst() + k == i) {
				queue.removeFirst();
			}

			if (i >= k - 1) {
				res[j++] = nums[queue.getFirst()];
			}

		}
		return res;
	}

	public static void main(String args[]) {
		System.out.println(maxSlidingWindow(new int[] { 4, 3, 2, 0, 5, 9, 1, 0 }, 3));
	}

}
