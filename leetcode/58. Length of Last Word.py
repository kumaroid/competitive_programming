class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        string = s.split(" ")
        while(string.count("")):
            string.remove("")
        return len(string[-1])
