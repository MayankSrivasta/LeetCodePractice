class Solution:

    # two pointer approach
    def isPalindrome(self, s: str) -> bool:
        # Initialize two pointers
        left, right = 0, len(s) - 1
        
        while left < right:
            # Skip non-alphanumeric characters (left pointer)
            while left < right and not s[left].isalnum():
                left += 1
            # Skip non-alphanumeric characters (right pointer)
            while left < right and not s[right].isalnum():
                right -= 1
            
            # Compare lowercase characters
            if s[left].lower() != s[right].lower():
                return False
            
            # Move pointers inward
            left += 1
            right -= 1
        
        return True


# reverse string
    def isPalindrome(self, s: str) -> bool:
        newStr = ''
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]
    

#     The general syntax of slicing is:
#     string[start:stop:step]
#     start: Starting index (optional, defaults to 0).
#     stop: Ending index (optional, defaults to the end of the string).
#     step: The increment between elements. If -1, it iterates in reverse order.