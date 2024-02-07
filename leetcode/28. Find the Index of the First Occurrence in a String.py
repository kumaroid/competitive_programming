class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1

        res = haystack.replace(needle, "$")
        for i in range(len(res)):
            if res[i] == "$":
                return i
