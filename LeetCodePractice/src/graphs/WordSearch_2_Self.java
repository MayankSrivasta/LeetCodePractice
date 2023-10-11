package graphs;

import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Set;

import graphs.WordSearch2_Self.TrieNode;

public class WordSearch_2_Self {

	public class TrieNode {
		public boolean isWord = false;
		public TrieNode[] child = new TrieNode[26];

		public TrieNode() {

		}
	}

	TrieNode root = new TrieNode();
	boolean[][] flag;

	public List<String> findWords(char[][] board, String[] words) {
		Set<String> result = new HashSet<>();
		flag = new boolean[board.length][board[0].length];

		addToTrie(words);

		for (int i = 0; i < board.length; i++) {
			for (int j = 0; j < board[0].length; j++) {
				if (root.child[board[i][j] - 'a'] != null) {
					search(board, i, j, root, "", result);
				}
			}
		}

		return new LinkedList<>(result);
	}
//	below line is like iteration - like going from top to bottom, going to the child node
//	below line is like iterating the linked-list
	private void addToTrie(String[] words) {
		for(String word : words)
		{
			
//			whenever a new word comes it needs to be added to the root of the 
//			trieNode
			TrieNode node = root;
			for(char ch : word.toCharArray())
			{
				if(node.child[ch - 'a'] == null)
					node.child[ch - 'a'] = new TrieNode();
				
//				below line is like iteration - like going from top to bottom, going to the child node
//				below line is like iterating the linked-list
				node = node.child[ch - 'a'];
			}
			node.isWord = true;
		}
	}

	private void search(char[][] board, int i, int j, TrieNode node, String word, Set<String> result) {

		if (i >= 0 && j >= 0 && i < board.length && j < board[0].length && node.child[board[i][j] - 'a'] != null && !flag[i][j]) {

			flag[i][j] = true;
//			traversing to the child of the node
			node = node.child[board[i][j] - 'a'];
			if (node.isWord)
				result.add(word + board[i][j]);
			
//			in the below codes we are sending -> " word + board[i][j] ", this means that if the specific character is found we are going to add it
//			to the word & if the complete word is found at the line 63 we are going to add the complete word in the HashSet.
			search(board, i - 1, j, node, word + board[i][j], result);
			search(board, i + 1, j, node, word + board[i][j], result);
			search(board, i, j - 1, node, word + board[i][j], result);
			search(board, i, j + 1, node, word + board[i][j], result);

			flag[i][j] = false;

		}

	}

}
