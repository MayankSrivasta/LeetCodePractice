package graphs;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class AdjacencyList_Self {
	
	
	static void addEdge(ArrayList<ArrayList<Integer>> list, int u, int v)
	{
		list.get(u).add(v);
		list.get(v).add(u);
	}
	
	
	static void printGraph(ArrayList<ArrayList<Integer>> list)
	{
		for(int i = 0; i < list.size(); i++)
		{
			for (int j = 0; j < list.get(i).size(); j++) {
				System.out.print(" " + list.get(i).get(j));
			}
			System.out.println();
		}
	}
	
	public static void main(String args[])
	{
		int v = 5;
		
		ArrayList<ArrayList<Integer>> adj = new ArrayList<ArrayList<Integer>>(v);
		
		for(int i = 0; i < v; i++)
		{
			adj.add(new ArrayList<Integer>());
		}
		
		addEdge(adj, 0, 1);
        addEdge(adj, 0, 4);
        addEdge(adj, 1, 2);
        addEdge(adj, 1, 3);
        addEdge(adj, 1, 4);
        addEdge(adj, 2, 3);
        addEdge(adj, 3, 4); 
		
		printGraph(adj);
		
	}
}
