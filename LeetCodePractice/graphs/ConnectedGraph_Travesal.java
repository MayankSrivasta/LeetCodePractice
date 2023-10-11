package graphs;

import java.util.*;

public class ConnectedGraph_Travesal {

	static void addEdge(ArrayList<ArrayList<Integer>> adj, int u, int v) {
		adj.get(u).add(v);
		adj.get(v).add(u);
	}

	
	public static void main(String[] args) {
		int V = 7;
		ArrayList<ArrayList<Integer>> adj = new ArrayList<ArrayList<Integer>>(V);

		for (int i = 0; i < V; i++)
			adj.add(new ArrayList<Integer>());

		addEdge(adj, 0, 1);
		addEdge(adj, 0, 2);
		addEdge(adj, 2, 3);
		addEdge(adj, 1, 3);
		addEdge(adj, 1, 4);
		addEdge(adj, 3, 4);

		System.out.println("Following is Depth First Traversal: ");
		new Dfs_Traversal().DFS(adj, V, 0);
		
		System.out.println();
		System.out.println("Following is BFS Traversal: ");
		BFS_traversal bfs = new BFS_traversal();
//		bfs.bfsTraversal(adj, V, 0);
		
		bfs.BFS_traversal(adj, 0, V);
		
	}
}
