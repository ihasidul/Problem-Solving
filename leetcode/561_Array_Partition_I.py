class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum([_ for _ in sorted(nums)[::2]])