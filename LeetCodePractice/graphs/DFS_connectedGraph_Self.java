package graphs;

import java.util.ArrayList;

public class DFS_connectedGraph_Self {

	static void addEdge(ArrayList<ArrayList<Integer>> list, int u, int v) {
		list.get(u).add(v);
		list.get(v).add(u);
	}

	static void DFSRec(ArrayList<ArrayList<Integer>> list, int v, boolean[] visited) {
		visited[v] = true;
		System.out.println("Visited " + v);
		for (int u : list.get(v)) {
			if (visited[u] == false)
				DFSRec(list, u, visited);
		}
	}

	static void DFS(ArrayList<ArrayList<Integer>> list, int v, int u)
	{
		boolean[] visited = new boolean[v];
		
		for(int i = 0; i < v; i++)
			visited[i] = false;
		
		DFSRec(list,u,visited);
		
	}

	public static void main(String args[]) 
	{
		int v = 5;
		ArrayList<ArrayList<Integer>> list = new ArrayList<>();

		for (int i = 0; i < v; i++)
			list.add(new ArrayList<Integer>());
		
		addEdge(list, 0, 1);
		addEdge(list, 0, 2);
		addEdge(list, 2, 3);
		addEdge(list, 1, 3);
		addEdge(list, 1, 4);
		addEdge(list, 3, 4);
		
		System.out.println(" Starting DFS ");
		 DFS(list,v,0);
	}

}
