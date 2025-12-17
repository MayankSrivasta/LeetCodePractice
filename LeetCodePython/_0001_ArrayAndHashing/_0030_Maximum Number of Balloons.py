from collections import defaultdict
from collections import Counter
class Solution:
    # neetcode solution         https://neetcode.io/solutions/maximum-number-of-balloons
    # solution - 1
    def maxNumberOfBalloons(self, text: str) -> int:
        mp = defaultdict(int)
        for c in text:
            if c in "balon":
                mp[c] += 1
        
        if len(mp) < 5:
            return 0
        
        mp['l'] //= 2
        mp['o'] //= 2
        return min(mp.values())

    # chatgpt solution
    # solution - 2
    def maxNumberOfBalloons(self, text: str) -> int:
        counts = Counter(text)
        # Retrieve counts for 'b', 'a', 'l', 'o', 'n'
        return min(counts[ord('b') - ord('a')],
                   counts[ord('a') - ord('a')],
                   counts[ord('l') - ord('a')] // 2,
                   counts[ord('o') - ord('a')] // 2,
                   counts[ord('n') - ord('a')])

# solution - 3
# BEST AND EASY TO UNDERSTAND SOLUTIONS
    def maxNumberOfBalloons(self, text: str) -> int:
        textCount = Counter(text)
        ballCount = Counter("balloon")
        res = float('inf')
        for c in ballCount:
            res = min(res, textCount[c] // ballCount[c])
        return res


    def maxNumberOfBalloons(self, text: str) -> int:
        # Count the frequency of each character in the input text
        char_count = Counter(text)
        
        # Adjust the counts for 'l' and 'o' since we need 2 of each
        char_count['l'] //= 2
        char_count['o'] //= 2
        
        # Find the minimum count among the required characters
        return min(char_count['b'], char_count['a'], char_count['l'], char_count['o'], char_count['n'])


sol = Solution()
print(sol.maxNumberOfBalloons("nlaebolko"))
print(sol.maxNumberOfBalloons("loonbalxballpoon"))
print(sol.maxNumberOfBalloons("loonbalxballpoon"))  # Output: 2