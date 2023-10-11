package graphs;

public class WordSearch_Self {
	
    public boolean exist(char[][] board, String word) {
     
    	int count = 0;
    	
    	if(board.length == 0)
    		return false;
    	
    	for(int i = 0; i < board.length; i++)
    	{
    		for(int j = 0; j < board[0].length; j++)
    		{
    			if(board[i][j] == word.charAt(0) && dfs(board, i, j, word, count))
    				return true;
    		}
    	}
    	
    	
    	return false;
    }
	
	boolean dfs(char[][] board, int i, int j, String word, int count)
	{
		boolean status = false;
		
		if(word.length() == count)
			return true;
		
		if(i >= 0 && j >= 0 && i < board.length && j < board[0].length && board[i][j] == word.charAt(count))
		{
			
			char temp = board[i][j];
			board[i][j] = '#';
			count++;
			status = 	dfs(board, i + 1, j, word, count) ||
						dfs(board, i - 1, j, word, count) ||
						dfs(board, i, j + 1, word, count) ||
						dfs(board, i, j - 1, word, count);
			board[i][j] = temp;
			
			
		}
		
		return status;
		
	}
}
