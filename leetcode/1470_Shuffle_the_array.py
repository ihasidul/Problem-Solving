class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        y_half = nums[len(nums)//2 :]
        #print(y_half)
        nl = []
        for _ in range(n):
            nl.append(nums[_])
            nl.append(y_half[_])
            
        return nl