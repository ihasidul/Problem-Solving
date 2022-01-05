class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pointer = 0
        pointer2 = 1
        
        for i in range(len(nums)-1):
            if nums[i] != nums[i + 1]:
                pointer += 1
                nums[pointer] = nums[i + 1]
        print(nums)
        print(pointer)
        for i in range(pointer,len(nums)-1):
            nums[i + 1] = '_'
        print(nums)


# It is a test line 
