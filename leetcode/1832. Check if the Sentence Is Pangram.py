class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        if set(alph) == set(sentence):
            return True
        return False
