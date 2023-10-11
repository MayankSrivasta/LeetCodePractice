package graphs;

import java.util.LinkedList;
import java.util.Queue;

public class NoOfProvidence {

//	keep in mind the reason for using 2 for loops is that - 
//	the 1st loop is going to pick the vertices & the 2nd loop is going to check & find if there exist the connection between the 
//	vertice found in the 1st loop to the 2nd loop
	
//	BFS Approach
	public int findCircleNum_BFS_Approach(int[][] M) {
		
		int count = 0;
		boolean[] visited = new boolean[M.length];
		Queue<Integer> q = new LinkedList<>();
		
		for(int i = 0; i < M.length; i++)
		{
			if(!visited[i])
			{
				q.add(i);
				
				while(!q.isEmpty())
				{
					
//					remember y ur setting visited[p] here & not inside the if(M[i][j] == 1 && !visited[j]) condition is that
//					is that here ur polling the value out of the queue & utilising/further using it because of which
//					ur setting the visited[p] = true
					
					int p = q.poll();
					visited[p] = true;
					
					for(int j = 0; j < M.length; j++)
					{
						if(M[p][j] == 1 && !visited[j])
						{
							q.add(j);
						}
					}	
				}
				//similar condition applies from the DFS to here case. when there is disconnection in between the vertices
//				& we have to go to the 'for' loop to iterate & find the next vertice then we increase count value
				count++;
			}
		}
		return count;
	}
	
//	################################################
//	DFS approach
	
	    public int findCircleNum_DFS_Approach(int[][] m) {
	        int count = 0;
	        boolean[] visited = new boolean[m.length];
	        
	        for(int i = 0; i < m.length; i++)
	        {
	        	
	            if(!visited[i])
	            {
	            	//very important thing that why we are counting insited the visited condition is that, since
//		        	we are iterating the vertices in the above for loop & if the vertices are connected then the DFSRec function 
//		        	will keep on going & if at any case the recursion is completed it will return, 
//		        	so in case the vertices which are not connected DFSRec function will be returned/exit ,
//		        	& again the for loop will staart with the vertices which are not visited,
//		        	since the loop iis going to increment which means that the vertices are not connected & 
//		        	we have to iterate the vertices using the for loop.
		        	
	            	
	            	count++;
	                DFSRec(m, i, visited);
	            }
	        }
	        return count;
	    }
	    
//	    in this method whatever the vertices are connected are going to be traversed in DFS approach
	    public void DFSRec(int[][] m, int i, boolean[] visited)
	    {
	        visited[i] = true;
	        
	        for(int j = 0; j < m.length; j++)
	        {
	            if(m[i][j] == 1 && !visited[j])
	            {
	                DFSRec(m, j, visited);
	            }
	        }
	    }
	    
	
	
	
}
