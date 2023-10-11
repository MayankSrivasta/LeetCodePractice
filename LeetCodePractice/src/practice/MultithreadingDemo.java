package practice;

import myexceptionlist.AlreadyFilledException;

//Java code for thread creation by extending
//the Thread class
class MultithreadingDemo implements Runnable {

	public MultithreadingDemo(int[][] arr, int i, int j) {


		if (arr[i][j] != 0) {
			try {
				throw new AlreadyFilledException("Cell is Occupied");

			} catch (AlreadyFilledException e) {
				System.out.println(e.getMessage());

			}
		}
		else
		{
			System.out.println("cell is not occupied ");
		}

	}

	@Override
	public void run() {

		try {
			// Displaying the thread that is running
			System.out.println("Thread " + Thread.currentThread().getId() + " is running");

			throw new AlreadyFilledException("Cell is Occupied");

		} catch (AlreadyFilledException e) {
			System.out.println(e.getMessage());

		}
	}
}
