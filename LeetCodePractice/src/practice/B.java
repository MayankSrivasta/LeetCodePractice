package practice;

public class B implements InterfaceA {

	public static void method1() {
		System.out.println("Method-1 of the B class is executed.");
	}

	public void method2() {
		System.out.println("Method-2 of the B class is executed.");
	}

	public static void main(String args[]) {
//		A d1 = new A();
//		d1.method1();
//		d1.method2();

		B b = new B();
		b.method1();

		// d2 is reference variable of class Demo that points to object of class Sample
//		A d2 = new B();
//		// method calling with reference (method hiding)
//		d2.method1();
//		// method calling with object (method overriding)
//		d2.method2();
	}
}
