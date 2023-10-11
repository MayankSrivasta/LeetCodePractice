package myexceptionlist;

public class AlreadyFilledException extends Exception {
	
	
	public AlreadyFilledException (String str)  
    {  
        // calling the constructor of parent Exception  
        super(str);
        
    }
}
