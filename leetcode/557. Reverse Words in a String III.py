class Solution:
    def reverseWords(self, s: str) -> str:
        string = s.split()
        tmp = ''
        for char in string:
            tmp += char[::-1]
            tmp += ' '
        return tmp[:-1]
