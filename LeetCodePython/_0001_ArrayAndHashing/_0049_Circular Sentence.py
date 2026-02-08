class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        w = sentence.split(" ")

        for i in range(len(w)):
# w[i - 1] will be a bit confusing here because since i = 0, it will refer to i = -1,
# which should give index out of bound error, but it will not, in python it will refer to the last 
# word in the string
            if w[i][0] != w[i - 1][-1]:
                return False
        return True
    
#   another approach:-  check neetcode.io video if not able to understand
#   https://www.youtube.com/watch?v=9Ty_eRjoDNM
    def isCircularSentence(self, sentence: str) -> bool:
        for i in range(len(sentence)):
            if sentence[i] == " " and sentence[i - 1] != sentence[i + 1]:
                return False
        return sentence[0] == sentence[-1]
    
#====================================================================================================

# chatgpt
def isCircularSentence(sentence: str) -> bool:
    words = sentence.split()
    n = len(words)

    for i in range(n):
        curr_last = words[i][-1]
        next_first = words[(i + 1) % n][0]  # wraps around circularly
        if curr_last != next_first:
            return False

    return True
