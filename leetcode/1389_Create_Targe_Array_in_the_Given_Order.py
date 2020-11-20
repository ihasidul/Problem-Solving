class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        lst =  []
        for _ in range(len(nums)):
            lst.insert(index[_], nums[_])
            print("index[i]", index[_])
            print("nums[i]", nums[_])
            print("-----------------------------------")
        return lst