package leetCode;

import java.util.Arrays;
import java.util.Scanner;

public class NNumbers {
	
	static int n;
	static int p[];
	static int result[];
	NNumbers(int n, int p[])
	{
		this.n = n;
		this.p = p;
	}
	 
	 static int[] findPrimeFactors()
	 {
		
		 for(int j = 0; j < n; j++)
		 {
			 int k = 0;
			 int temp[] = new int[50];
			 int number = p[j];
			 
		 for(int i = 2; i< number; i++) 
		 {
	         while(number%i == 0) 
	         {
	        	temp[k++] = i;
//	            System.out.println(i+" ");
	            number = number/i;
	         }
	      }
		 if(number >2) {
			 temp[k++] = number;
//	         System.out.println(number);
	      }
		 
		 System.out.println(Arrays.toString(remove(temp)));

		 }
		 
		 		 
		 return new int[] {};
	 }
	 
	 public static void main(String args[])
	 {
		 Scanner input = new Scanner(System.in);
		 System.out.println("enter size");
		 int size = input.nextInt();
		 int arr[] = new int[size];
		 for(int i = 0; i < size; i++) 
		 {
			 System.out.println("enter nos");
			 arr[i] = input.nextInt();
		 }
		 
		 NNumbers object = new NNumbers(size, arr);
		 findPrimeFactors();
		 
		 
	 }
	 
	static int[] remove(int k[] )
	 {
		 int count = 0;
		 for(int i = 0; i < k.length; i++)
		 {
			 if(k[i] != 0)
			 {
				 count++;
			 }
		 }
		 
		 int tem[] = new int[count];
		 for(int i = 0; i < count; i++)
		 {
			 tem[i] = k[i];
		 }
		 return tem;
	 }

}
