package graphs;

import java.util.List;

public class KeysAndRooms_DFS_Recursion_MostEfficient {

	private int dfs(int cur, List<List<Integer>> edges, boolean[] visited) {

//	         ret is counting the no. of vertices are vertices visited & if the 
//	         returned vertices == room.size() then the all the vertices are visited, 
//	         so rather than again iterating & checking each of the vertices are true/false
//	         simply here we are counting the size

		int ret = 1;
		visited[cur] = true;
		for (int next : edges.get(cur)) {
			if (!visited[next]) {
				ret += dfs(next, edges, visited);
			}
		}
		return ret;
	}

	public boolean canVisitAllRooms(List<List<Integer>> rooms) {
		return dfs(0, rooms, new boolean[rooms.size()]) == rooms.size();
	}
}
