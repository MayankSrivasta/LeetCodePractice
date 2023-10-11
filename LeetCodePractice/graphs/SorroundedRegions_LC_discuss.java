package graphs;

public class SorroundedRegions_LC_discuss {

	int[][] dirs = { { 0, 1 }, { 1, 0 }, { 0, -1 }, { -1, 0 } };
	int r, c;

	public void solve(char[][] board) {
		r = board.length;
		if (r < 3)
			return;
		c = board[0].length;
		if (c < 3)
			return;

		int x = 0, y = 0;
		for (int i = 0; i < 4;) {
			while (x >= 0 && x < r && y >= 0 && y < c) {
				if (board[x][y] == 'O') {
					dfs(x, y, board);
				}
				x += dirs[i][0];
				y += dirs[i][1];
			}
			x -= dirs[i][0];
			y -= dirs[i][1];
			i++;
		}
		for (int i = 0; i < r; i++) {
			for (int j = 0; j < c; j++) {
				if (board[i][j] == 'O')
					board[i][j] = 'X';
				else if (board[i][j] == 'Z')
					board[i][j] = 'O';
			}
		}
	}

	void dfs(int x, int y, char[][] board) {
		board[x][y] = 'Z';
		for (int i = 0; i < 4; i++) {
			int m = x + dirs[i][0];
			int n = y + dirs[i][1];
			if (m >= 0 && m < r && n >= 0 && n < c && board[m][n] == 'O') {
				dfs(m, n, board);
			}
		}
	}

}
