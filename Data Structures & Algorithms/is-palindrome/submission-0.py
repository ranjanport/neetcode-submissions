class Solution:
    def isPalindrome(self, s: str) -> bool:
        format_str = ""
        for char in s:
            if char.isalnum():
                format_str+=char.lower()
        
        left, right = 0, len(format_str)-1
        
        while left < right:
            if format_str[left] == format_str[right]:
                left+=1
                right-=1
            else:
                return False
        return True
        