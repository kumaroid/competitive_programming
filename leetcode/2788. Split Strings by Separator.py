class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        ans = []
        for word in words:
            s = ""
            for i, char in enumerate(word):
                if char != separator:
                    s += char
                else:
                    if s:
                        ans.append(s)
                        s = ""
            if s:
                ans.append(s)
        return ans
