class Solution:
    
    # chatgpt solution
    
    # res = [] → Stores the result (justified text).
    # line = [] → Holds words for the current line.
    # line_len = 0 → Tracks total length of words (excluding spaces).

    # len(line) - returns the no. of words in current line, this will help to figure out the no.
    # of space required

    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        res, line, line_len = [], [], 0
        
        for word in words:
            if line_len + len(word) + len(line) - 1 >= maxWidth:
                # Distribute spaces evenly
                for i in range(maxWidth - line_len):
                    gaps = (len(line) - 1 or 1)     #in case either multiple words are given or single word
                    index = i % gaps
                    line[index] += " "
                res.append("".join(line))
                line, line_len = [], 0  # Reset for next line
            
            line.append(word)
            line_len += len(word)

        # Handle the last line (left-justified)
        res.append(" ".join(line).ljust(maxWidth))
        return res

print(Solution().fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))