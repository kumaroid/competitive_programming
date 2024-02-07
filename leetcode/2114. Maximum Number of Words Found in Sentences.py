class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        mx = 0
        for row in sentences:
            if row.count(" ") > mx:
                mx = row.count(" ")
        return mx + 1
