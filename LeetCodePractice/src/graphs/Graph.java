package graphs;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

public class Graph {
	
	
	static void DFS(ArrayList<ArrayList<Integer>> list, int u, boolean visited[])
	{
		visited[u] = true;
		System.out.print(u + "");
		
		for(int i : list.get(u))
			if(!visited[i])
				DFS(list, i, visited);
		
	}
	
	static void BFS(ArrayList<ArrayList<Integer>> adj)
	{
		
		boolean[] visited = new boolean[adj.size()];
		
		Queue<Integer> q = new LinkedList<>();
		
		q.add(0);
		visited[0] = true;
		
		while(!q.isEmpty())
		{
			int p = q.poll();
			
			for(int i : adj.get(p))
				if(!visited[i])
				{
					q.add(i);
					visited[i] = true;
				}
		}
		
		
		
	}
	
}
