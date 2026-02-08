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
    # testing github
#====================================================================================================

# reverse string
    def isPalindrome(self, s: str) -> bool:
        new = []
        for c in s:
            if c.isalnum():
                new.append(c.lower())

        return new == new[::-1]

# Examples:
# s[::2] → every other char
# s[1::] → from index 1 to end
# s[:3] → first 3 characters
# s[::-1] → reversed

# ✔ new[::-1] creates a new reversed string/list
# ✔ Does NOT reverse in-place
# ✔ So time = O(n), space = O(n)

#     The general syntax of slicing is:
#     string[start:stop:step]
#     start: Starting index (optional, defaults to 0).
#     stop: Ending index (optional, defaults to the end of the string).
#     step: The increment between elements. If -1, it iterates in reverse order.