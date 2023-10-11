package graphs;

class NumberOfIslands {

	public int numIslands(char[][] grid) {

		if (grid == null || grid.length == 0)
			return 0;

		int island = 0;

		for (int i = 0; i < grid.length; i++) {
			for (int j = 0; j < grid[0].length; j++) {
				if (grid[i][j] == '1') {
					dFS(grid, i, j);
					island++;
				}

			}
		}
		return island;
	}

	private void dFS(char[][] grid, int i, int j) {
		if (i >= 0 && j >= 0 && i < grid.length && j < grid[0].length && grid[i][j] == '1') {
			grid[i][j] = '0';
			dFS(grid, i + 1, j);
			dFS(grid, i - 1, j);
			dFS(grid, i, j + 1);
			dFS(grid, i, j - 1);
		}
	}

}
