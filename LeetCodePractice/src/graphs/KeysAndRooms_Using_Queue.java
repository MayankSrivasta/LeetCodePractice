package graphs;

import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class KeysAndRooms_Using_Queue {

	public boolean canVisitAllRooms(List<List<Integer>> rooms) {

		boolean visited[] = new boolean[rooms.size()];
		Queue<Integer> q = new LinkedList<Integer>();

		q.add(0);
		visited[0] = true;

		while (!q.isEmpty()) {

			int p = q.poll();

			for (int i : rooms.get(p))
				if (visited[i] == false) {
					q.add(i);
					visited[i] = true;
				}
		}

		for (int i = 0; i < rooms.size(); i++) {
			if (!visited[i])
				return false;
		}

		return true;

	}
}
