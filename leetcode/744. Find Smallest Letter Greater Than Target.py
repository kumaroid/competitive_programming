class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        return min(a) if len(a := list(filter(lambda x: x>target, letters))) > 0 else letters[0]
