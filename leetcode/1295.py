# 1295. Find Numbers with Even Number of Digits

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for _ in nums:
            s = str(_)
            if(len(s)%2 == 0):
                count += 1
            else:
                continue
        return count