package leetCode;

import java.util.HashMap;
import java.util.Map;

public class BullsCows {

	
	public static void main(String args[])

	{
		System.out.println(getHint2("1231","0111"));
	}

	    public static String getHint(String secret, String guess) {
	        
	    	HashMap<Character, Integer> h = new HashMap();
	        
	        for (char s : secret.toCharArray()) 
	        {
	            h.put(s, h.getOrDefault(s, 0) + 1);
	        }
	            
	        int bulls = 0, cows = 0;
	        int n = guess.length();
	        
	        for (int idx = 0; idx < n; ++idx) 
	        {
	            char ch = guess.charAt(idx);
	            
	            if (h.containsKey(ch)) 
	            {
	                // corresponding characters match
	                if (ch == secret.charAt(idx)) 
	                {
	                    bulls++;

	                    
//	                    The update of the cows is needed if the count for the current character in the hashmap is negative or equal to zero.
//	                    That means that before it was already used for cows, and the cows counter should be decreased: cows -= int(h[ch] <= 0).
//	                    "1231","0111"
//	                    it is in this case that 1 which is present in the 2nd position in the guess and has been updated as cows, but the 1 which is
//	                    present in the 4th position in the guess is found as equals positions in both the strings, so cows is updated
	                    
	                    if (h.get(ch) <= 0)
	                        cows--;    
	                // corresponding characters don't match
	                } 
	                else 
	                {
//	                	this line checks whether the guess key is present in the hashmap & not negative, or not & accordingly update the cows
	                	if (h.get(ch) > 0)
	                        cows++;     
	                }
	                // ch character was used
	                h.put(ch, h.get(ch) - 1); 
	            }
	        }
	                
	        return Integer.toString(bulls) + "A" + Integer.toString(cows) + "B";
	    }
	
	
	
	
	public String getHint1(String secret, String guess) 
	{
		String str = "";
		int bulls = 0, cows = 0;
		
		Map<Character, Integer> hm = new HashMap<>();
		
		for(int i = 0; i < secret.length(); i++)
		{
			hm.put(secret.charAt(i), hm.getOrDefault(secret.charAt(i), 0) + 1);
		}
		
		for(int i = 0; i < guess.length(); i++)
		{
			char g = guess.charAt(i);
			
			if(hm.containsKey(g))
			{
				if(g == secret.charAt(i))
				{
					bulls++;
					
					if(hm.get(g) < 0)
						cows--;
				}
				else
				{
					if(hm.get(g) > 0)
						cows++;
				}
				
				hm.put(g, hm.get(g) - 1);
			}
		}
		
		
		return str;
		
	}
	
	  public static String getHint2(String secret, String guess) {
	        int bulls =0;
	        int cows =0;
	        int[] secretFreq =new int[10];

	        int[] guessFreq =new int[10];

	        // O(n)
	        for(int i=0;i<secret.length();i++){
	            char secretChar = secret.charAt(i);

	            char guessChar = guess.charAt(i);

	            if(secretChar == guessChar){
	                bulls++;
	            } else{
	                secretFreq[secretChar -'0']++;

	                guessFreq[guessChar -'0']++;
	            }
	        }

	        // O(1)
	        for(int i=0;i<10;i++){
	            cows += Math.min(secretFreq[i], guessFreq[i]);
	        }

	        return bulls +"A"+ cows +"B";
	    }

}
