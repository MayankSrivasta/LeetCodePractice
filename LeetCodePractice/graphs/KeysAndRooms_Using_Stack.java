package graphs;

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

//using stack approach is not any beneficial

public class KeysAndRooms_Using_Stack {
	
	
	public boolean canVisitAllRooms(List<List<Integer>> rooms) 
	{
		boolean[] seen = new boolean[rooms.size()];
		seen[0] = true;
		Stack<Integer> stack = new Stack<>();
		stack.push(0);

		// At the beginning, we have a todo list "stack" of keys to use.
		// 'seen' represents at some point we have entered this room.
		while (!stack.isEmpty()) { // While we have keys...
			int node = stack.pop(); // Get the next key 'node'
			for (int nei : rooms.get(node)) // For every key in room # 'node'...
				if (!seen[nei]) { // ...that hasn't been used yet
					seen[nei] = true; // mark that we've entered the room
					stack.push(nei); // add the key to the todo list
				}
		}

		for (boolean v : seen) // if any room hasn't been visited, return false
			if (!v)
				return false;
		return true;
	}
	
//	#############################################################################
	
	static void DFSRec(ArrayList<ArrayList<Integer>> adj, int s, boolean[] visited) {
		visited[s] = true;
		
		for (int u : adj.get(s))
			if (visited[u] == false)
				DFSRec(adj, u, visited);

	}

	static void DFS(ArrayList<ArrayList<Integer>> adj) {

		boolean[] visited = new boolean[adj.size()];

		DFSRec(adj, 0, visited);
	}

}
