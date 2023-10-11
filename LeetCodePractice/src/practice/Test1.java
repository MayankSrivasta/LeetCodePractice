package practice;

import java.util.Scanner;

class Test1 {

	public static void main(String args[])
	{
		
		Scanner input = new Scanner(System.in);
		double output = 0;
		int n = input.nextInt();
		
		if(n <= 100)
		{
			System.out.println(0.0+"INR");
		}
		else if( n > 100 && n <= 200)
		{
			output += (n * 1.5 - 150);
			
			output += 20;
			System.out.println(output+"INR");
		}
		else if(n > 200 && n <=500)
		{
			output += 150;
			n -= 100;
			
			output += 200;
			n -= 100;
			
			output += n*3;
			
			output += 30 - 150;
			
			System.out.println(output+"INR");
		}
		else if(n > 500)
		{
			output = 150;
			
			output += 350;

			output += 1380;
		
			output += ((n - 500) * 6.6);
			
			output += 50 - 150;
			
			System.out.println(output+"INR");
			
		}
		
	}
	
	
}
