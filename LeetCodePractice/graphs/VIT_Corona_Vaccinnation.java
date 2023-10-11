package graphs;

import java.util.LinkedList;
import java.util.Queue;

public class VIT_Corona_Vaccinnation {

	public static void main(String args[]) {
		Queue<Employee> mainList = new LinkedList<Employee>();
		Queue<Employee> firstDoseList = new LinkedList<>();
		Queue<Employee> secondDoseList = new LinkedList<>();
		
		
		createMainList(mainList);
		System.out.println("Printing MainList");
		printList(mainList);
		
		System.out.println("Printing FirstList");
		createList(mainList, firstDoseList, secondDoseList);
		printList(firstDoseList);
		
		System.out.println("Printing SecondList");
		printList(secondDoseList);
		

	}

	static void createMainList(Queue<Employee> mainList) {
		mainList.add(new Employee("Mayank", "001", "Y"));
		mainList.add(new Employee("Advika", "002", "N"));
		mainList.add(new Employee("Rahul", "003", "Y"));
		mainList.add(new Employee("Kumar", "004", "N"));
	}

	static void printList(Queue<Employee> list) {
		for (Employee e : list)
			System.out.println(e);
	}

	static void createList(Queue<Employee> list ,Queue<Employee>  firstDoseList, Queue<Employee>  secondDoseList )
	{
		for(Employee e : list)
		{
			if(e.getStatus().equalsIgnoreCase("Y"))
				firstDoseList.add(e);
			else
				secondDoseList.add(e);
		}	
	}
}
