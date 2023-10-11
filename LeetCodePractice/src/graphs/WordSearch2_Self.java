package graphs;

import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Set;

public class WordSearch2_Self {
	
	class TrieNode {
		boolean isWord;
		TrieNode child[] = new TrieNode[26];
	}
	
	TrieNode root = new TrieNode();
	boolean[][] flag;
	
	void addWords(String[] words)
	{
		for(String word : words)
		{
			TrieNode node = root;
			for(char ch : word.toCharArray()) 
			{
				if(node.child[ch - 'a'] == null)
					node.child[ch - 'a'] = new TrieNode();
				
				node = node.child[ch - 'a'];
			}
			node.isWord = true;
		}
	}
	
	List<String> findWords(char[][] board, String[] words)
	{
		Set<String> result = new HashSet<>();
		flag = new boolean[board.length][board[0].length];
		
		addWords(words);
		System.out.println(root);
		
		for(int i = 0; i < board.length; i++)
		{
			for(int j = 0; j < board[0].length; j++)
			{
				if(root.child[board[i][j] - 'a'] != null)
					search(board, i, j, "", root, result);	
			}
		}
		
	
		return new LinkedList<>(result);
	}
	
	void search(char[][] board, int i, int j, String word, TrieNode node, Set<String> result)
	{
		if( i >= 0 && j >= 0  && i < board.length && j < board[0].length && node.child[board[i][j] - 'a'] != null && !flag[i][j])
		{
			flag[i][j] = true;

			node = node.child[board[i][j] - 'a'];
			
			if(node.isWord)
				result.add(word + board[i][j]);
			
			
			search(board, i + 1, j, word + board[i][j], node, result);
			search(board, i - 1, j, word + board[i][j], node, result);
			search(board, i, j + 1, word + board[i][j], node, result);
			search(board, i, j - 1, word + board[i][j], node, result);
			
			flag[i][j] = false;
		}
		
	}
	
}
