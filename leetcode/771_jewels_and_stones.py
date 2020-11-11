class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        num = 0
        for _ in J:
            num += S.count(_)
        return num