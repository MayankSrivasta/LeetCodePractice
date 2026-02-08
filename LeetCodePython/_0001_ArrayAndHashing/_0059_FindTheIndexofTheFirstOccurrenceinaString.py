class Solution:

    # this solution is from neetcode youtube video & not from neetcode.io website
    # https://www.youtube.com/watch?v=Gjkhm1gYIMw
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        for i in range(len(haystack) + 1 - len(needle)):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1
    
#====================================================================================================


    # this might be from chatgpt
    def strStr(self, haystack: str, needle: str) -> int:
        # Length of the haystack and needle strings
        haystack_length, needle_length = len(haystack), len(needle)

        # Check all possible starting positions of needle in haystack
        for start in range(haystack_length - needle_length + 1):
            # If the substring matching the needle's length equals the needle, return the start index
            if haystack[start : start + needle_length] == needle:
                return start
      
        # If the needle is not found in haystack, return -1
        return -1

# The method strStr is intended to find the first occurrence of the needle string
# in the haystack string and return the index at which it begins.
# If needle is not part of haystack, it returns -1.