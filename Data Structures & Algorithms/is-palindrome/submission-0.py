class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        letters = ""
        reverse = ""

        for char in s:
            if char.isalnum():
                letters = letters + char.lower()
                reverse = char.lower() + reverse

        return letters == reverse
            