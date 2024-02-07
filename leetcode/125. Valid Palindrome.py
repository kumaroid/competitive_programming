# import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        h = ""
        for i in s:
            if i.isalpha() or i.isdigit():
                h += i
        string = h.lower()
        if string == string[::-1]:
            return True
        else:
            return False
