class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        w1 = ""
        w2 = ""
        for word in word1:
            w1 += word
        for words in word2:
            w2 += words
        return w1 == w2
