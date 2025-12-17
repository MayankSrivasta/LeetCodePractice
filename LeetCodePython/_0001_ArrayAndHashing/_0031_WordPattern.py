class Solution:

    # Input: pattern = "abba", s = "dog cat cat dog"
    # Output: true

    # this solution is same as ques 13-Isomorphic Strings
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(pattern) != len(words):
            return False
        charToWord = {}
        wordToChar = {}
        
        for c, w in zip(pattern, words):
            if ((c in charToWord and charToWord[c] != w) or (w in wordToChar and wordToChar[w] != c)):
                return False
            charToWord[c] = w
            wordToChar[w] = c
        return True
    
sol = Solution()
print(sol.wordPattern2("abba","dog cat cat dog"))


# ZIP USE
# names = ["Mayank", "Ravi", "Neha"]
# scores = [90, 85, 95]

# Mayank 90
# Ravi 85
# Neha 95