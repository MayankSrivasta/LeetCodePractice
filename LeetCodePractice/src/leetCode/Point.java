package leetCode;

public class Point {

	private final int x;
	private final int y;

	public Point(int x, int y) {

		this.x = x;
		this.y = y;
	}

	public int getX() {
		return x;
	}

	public int getY() {
		return y;
	}
	
	public static void main(String args[])
	{
		Point a = new Point(1,2);
		Point b = new Point(1,2);
		System.out.println(a.equals(b));

	}

}
