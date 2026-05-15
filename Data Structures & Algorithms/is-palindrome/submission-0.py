class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""
        for char in s:
            if char.isalnum(): #so doenst add spaces to cleaned
                cleaned += char.lower()
        reversed_string = cleaned[::-1] #reverses string
        return cleaned == reversed_string