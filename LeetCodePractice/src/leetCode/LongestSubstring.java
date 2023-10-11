package leetCode;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

public class LongestSubstring {
	
	public static void main(String args[])
	{
		System.out.println(longestSubstringSet("abcabcbb"));
	}
	
//	using set approach
	public static int longestSubstringSet(String str)
	{
		int max = 0;
		int a = 0;
		int b = 0;
		
		Set<Character> set = new HashSet();
		
		while(b < str.length())
		{
			if(!set.contains(str.charAt(b)))
			{
				set.add(str.charAt(b));
				max = Math.max(set.size(), max);
				b++;
			}
			else
			{
				set.remove(str.charAt(a));
				a++;
			}
		}
		
		
		return max;
	}
	
//	using hash approach
	public static int returnLength(String str)
	{
		int max = 0;
		int i = 0;
		
		Map<Character, Integer> hm = new HashMap();
		
		for(int j = 0; j < str.length(); j++)
		{
			if(hm.containsKey(str.charAt(j)))
				i = Math.max(j - i + 1, i);
			
			max = Math.max(j - i + 1 , max);
			hm.put(str.charAt(j), j + 1);
		}
		
		
		return max;
	}
	
	public static int lengthOfLongestSubstring(String str) 
	{

		int a = 0;
		int b = 0;
		int max = 0;
		Set<Character> set = new HashSet<>();
		while (b < str.length()) {
			if (!set.contains(str.charAt(b))) {
				set.add(str.charAt(b));
				b++;
				max = Math.max(set.size(), max);
			} else {
				set.remove(str.charAt(a));
				a++;
			}
		}
		return max;
	}
	
//	1st approach

	 public int lengthOfLongestSubstring1(String s) {
	       int ans = 0;
	        int i = 0;
	        HashMap<Character,Integer> hm = new HashMap<>();
	        for(int j = 0; j < s.length(); j++)
	        {
	            if(hm.containsKey(s.charAt(j)))
	                i = Math.max(hm.get(s.charAt(j)), i);
	                
	            ans = Math.max(ans, j - i + 1);
	            hm.put(s.charAt(j), j + 1);
	        }
	        return ans;
        
        
    }

//	2nd approach

	public int lengthOfLongestSubstring2(String s) {
	        int n = s.length(), ans = 0;
	        Map<Character, Integer> map = new HashMap<>(); // current index of character
	        // try to extend the range [i, j]
	        for (int j = 0, i = 0; j < n; j++) {
	            if (map.containsKey(s.charAt(j)))
	                // i = Math.max(map.get(s.charAt(j)), i);
	                i = map.get(s.charAt(j));
	    
	            ans = Math.max(ans, j - i + 1);
	            map.put(s.charAt(j), j + 1);
	        }
	        return ans;
	    }

//	3rd Approach- nick white
	public int lengthTest3(String str) 
	        {
	                Set<Character> set = new HashSet();
	                int len = str.length();
	                int a = 0;
	                int b = 0;
	                int max = 0;
	                while(b < len) 
	                {
	                        if(!set.contains(str.charAt(b)))
	                        {
	                                set.add(str.charAt(b));
	                                b++;
	                                max = Math.max(set.size(), max);
	                        }
	                        else {
	                                set.remove(str.charAt(a));
	                                a++;
	                        }        
	                }
	                return  max;
	        }
	        
	
	int longestString(String str)
	{
		int max = 0;
		
		Map<Character, Integer> hm = new HashMap();
		
		for(int j = 0; j < str.length(); j++)
		{
			
			
			
		}
		
		
		return max;
	}

}
