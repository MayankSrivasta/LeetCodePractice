package graphs;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

public class BFS_traversal {

	void bfsTraversal(ArrayList<ArrayList<Integer>> list, int v, int u) 
	{
		Queue<Integer> q = new LinkedList<>();
		boolean[] visited = new boolean[v];

//		for (int i = 0; i < v; i++)
//			visited[i] = false;

		q.add(u);
		visited[u] = true;

		while (!q.isEmpty()) 
		{
			int t = q.remove();
			System.out.print(t + " ");

			for (int i : list.get(t)) 
			{
				if (visited[i] == false) 
				{
					q.add(i);
					visited[i] = true;
				}

			}
		}

	}

	static void BFS_traversal(ArrayList<ArrayList<Integer>> list, int u, int v) 
	{
		
		boolean visited[] = new boolean[v];
//		for(int i = 0; i < v; i++)
//			visited[i] = false;
		
		Queue<Integer> q = new LinkedList<Integer>();
		
		//since we are entering the first value manually in the queue that's y its being set to true ( 0 is passed here )
		q.add(u);
		visited[u] = true;
		
		while(!q.isEmpty())
		{
			int p = q.poll();
			System.out.print(p);
			
			for(int i : list.get(p))
				if(visited[i] == false)
				{
					q.add(i);
					visited[i] = true;
				}
		}
	}

}
