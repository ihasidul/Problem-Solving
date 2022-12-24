class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = list(s)
        c = list(t)
        if len(s) != len(t):
            return False
        for char in letters:
            if char in c:
                c.remove(char)
        if len(c) == 0:
            return True
        return False
