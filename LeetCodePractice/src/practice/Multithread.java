package practice;

import java.util.Scanner;

import myexceptionlist.AlreadyFilledException;

//Main Class
public class Multithread {
	public static void main(String[] args) {
		try {

			test();

		} catch (AlreadyFilledException e) {
			System.out.println(e.getMessage());
			e.printStackTrace();
		}

	}

	public static void test() throws AlreadyFilledException {
		int arr[][] = new int[6][6];
		int k = 0, l = 0;

		for (int i = 0; i < 6; i++) {
			for (int j = 0; j < 6; j++) {
				arr[i][j] = 0;
			}
		}

		Scanner input = new Scanner(System.in);
		System.out.println("enter value 1st value");
		k = input.nextInt();
		System.out.println("enter value 1st value");
		l = input.nextInt();

		Runnable thread1 = new MultithreadingDemo(arr, k, l);
		new Thread(thread1).start();

		Runnable thread2 = new MultithreadingDemo(arr, k, l);
		new Thread(thread2).start();

	}

}
