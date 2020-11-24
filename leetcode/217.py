class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if(len(nums) == 0):
            return False
        num_dic = {}
        for _ in nums:
            num_dic[_] = 0
        for _ in nums:
            num_dic[_] = num_dic[_] + 1
        for (k,v) in num_dic.items():
            if(v > 1):
                return True      
        return False  