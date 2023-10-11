package practice;

public class BinarySearch {
	
	public static void main(String args[])
	{
		System.out.println(search(new int[] {-1,0,3,5,9,12}, 9))	;
	}
	
    public static int search(int[] nums, int target) 
    {
        int i = 0;
        int j = nums.length - 1;
        int k = 0;
        return binarySearch(i, j, k, nums, target);
        
    }
    
    static  int binarySearch(int i, int j, int k, int[] nums, int target)
    {
        k = (j - i) + i/ 2;
        
        if(nums[k] == target)
            return k;
        else if(nums[k] < target) 
        {
        	i = k;
            return binarySearch(i, j, k, nums, target);
        }
        else if(nums[k] > target)
        {
        	j = k;
        	return binarySearch(i, j, k, nums, target);
        }
        
        return -1;
    }

}
