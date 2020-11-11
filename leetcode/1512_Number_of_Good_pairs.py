class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        total = 0
        for _ in list(range(1, 100)):
            n = nums.count(_)
            #print(type(n))
            good = (n*(n - 1)) // 2
            total += good
        return total