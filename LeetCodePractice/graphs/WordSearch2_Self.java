package graphs;

public class WordSearch2_Self {
	
	class TrieNode
	{
		boolean isWord = false;
		TrieNode[] children = new TrieNode[26];
	}

	TrieNode root = new TrieNode();
	boolean[][] flag;
	
	void addToTrie(String[] words)
	{	
		for(String word : words)
		{
			TrieNode node = root;
			
			for(char ch : word.toCharArray())
			{
				if(node.children[ch - 'a'] == null)
					node.children[ch - 'a'] = new TrieNode();
				
				node = node.children[ch - 'a'];
			}
			
		}
	}
	
}
