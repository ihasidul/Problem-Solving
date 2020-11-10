class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        out = [] 
        sum = 0 
        for _ in nums:
            sum += _
            out.append(sum)
        return out