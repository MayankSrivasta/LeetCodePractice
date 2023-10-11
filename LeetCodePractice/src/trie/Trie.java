package trie;

class Trie {

//	CodeBix Trie Implementation
//	https://www.youtube.com/watch?v=T1M52UqQq3c&t=131s
	
	class TriNode {
		TriNode[] children = new TriNode[26];
		boolean isEnd = false;
	}

	TriNode root;

	public Trie() {
		root = new TriNode();
	}

	public void insert(String word) {
		TriNode node = root;
		for (int i = 0; i < word.length(); i++) {
			char c = word.charAt(i);
			if (node.children[c - 'a'] == null) {
				node.children[c - 'a'] = new TriNode();
			}
			node = node.children[c - 'a'];
		}
		node.isEnd = true;
	}

	public boolean search(String word) {
		TriNode node = root;
		for (int i = 0; i < word.length(); i++) {
			char c = word.charAt(i);
			if (node.children[c - 'a'] == null)
				return false;
			node = node.children[c - 'a'];
		}
		return node.isEnd;
	}

	public boolean startsWith(String prefix) {
		TriNode node = root;
		for (int i = 0; i < prefix.length(); i++) {
			char c = prefix.charAt(i);
			if (node.children[c - 'a'] == null)
				return false;
			node = node.children[c - 'a'];
		}
		return true;
	}
}
