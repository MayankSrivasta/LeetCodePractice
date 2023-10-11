package graphs;

import java.util.ArrayList;
import java.util.List;

public class Dfs_Traversal {

//	###########################################################
//	this one is solved using ADJACENCY LIST

	static void DFSRec(ArrayList<ArrayList<Integer>> adj, int s, boolean[] visited) {
		visited[s] = true;
		System.out.print(s + " ");

		for (int u : adj.get(s))
			if (visited[u] == false)
				DFSRec(adj, u, visited);

	}

	static void DFS(ArrayList<ArrayList<Integer>> adj, int V, int s)
	{

		boolean[] visited = new boolean[V];

		DFSRec(adj, s, visited);
	}

//	#######################################################
	
	
	public boolean canVisitAllRooms(List<List<Integer>> adj) 
	{

		boolean[] visited = new boolean[adj.size()];

		DFSRec(adj, 0, visited);
        
         for (boolean v : visited)
			if (!v)
				return false;
        
        
		return true;
        
	}
	
    
    
    	static void DFSRec(List<List<Integer>> adj, int s, boolean[] visited) {
		visited[s] = true;
		
		for (int u : adj.get(s))
			if (visited[u] == false)
				DFSRec(adj, u, visited);

	}
	
	
	
//	##########################################################
//	this one is solved using ADJACENCY MATRIXX
//	below one is just simple DFS algo
	
	public class Solution {
		public int findCircleNum(int[][] M) {
			int[] visited = new int[M.length];
			int count = 0;
			for (int i = 0; i < M.length; i++) {
				if (visited[i] == 0) {
					dfs(M, visited, i);
					count++;
				}
			}
			return count;
		}
	}

	public void dfs(int[][] M, int[] visited, int i) {
		for (int j = 0; j < M.length; j++) {
			if (M[i][j] == 1 && visited[j] == 0) {
				visited[j] = 1;
				dfs(M, visited, j);
			}
		}
	}
	
	static int DFSR(int[][] M)
	{
		int count = 0;
		
		boolean[] visited = new boolean[M.length];
		
		for(int i = 0; i < M.length; i++)
		{
			if(!visited[i])
			{
				count++;
				DFSRec2(M, i, visited);
			}
		}
		return count;
	}
	
	static void DFSRec2(int[][] M, int i , boolean[] visited)
	{
		
		for(int j = 0; j < M.length; j++)
		{
			if(M[i][j] == 1 && !visited[j])
			{
				visited[j] = true;
				DFSRec2(M, j, visited);
			}
		}
		
		
	}
	
}
