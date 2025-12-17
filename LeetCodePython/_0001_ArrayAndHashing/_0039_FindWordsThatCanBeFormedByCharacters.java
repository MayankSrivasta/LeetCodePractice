package _0001_ArrayAndHashing;

import java.util.HashMap;
import java.util.Map;

public class _0039_FindWordsThatCanBeFormedByCharacters {
    public static int countCharacters(String[] words, String chars) {
        Map<Character, Integer> count = new HashMap<>();
        for (char c : chars.toCharArray()) {
            count.put(c, count.getOrDefault(c, 0) + 1);
        }

        int res = 0;
        for (String word : words) {
            Map<Character, Integer> curWord = new HashMap<>();
            boolean good = true;
            // Iterate over each character in the word
            for (char c : word.toCharArray()) {
                curWord.put(c, curWord.getOrDefault(c, 0) + 1);
                // Check if character is in 'chars' and if the word uses it too many times
                if (!count.containsKey(c) || curWord.get(c) > count.get(c)) {
                    good = false;
                    break;
                }
            }
            // If the word is valid, add its length to the result
            if (good) {
                res += word.length();
            }
        }
        return res;
    }

    public static void main(String[] args) {
        System.out.println(countCharacters(new String[]{"cat", "bt", "hat", "tree"}, "atach"));
    }
}