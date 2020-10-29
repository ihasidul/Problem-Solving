class Solution:
    def two_sum(self, nums, target):
        seen = {}
        for i, v in enumerate(nums):
            remaining = target - v
            print(i, "Remaining: ",remaining)
            if remaining in seen:
                print("seen: ", seen)
                print("seen[remaining]:  ", seen[remaining])
                return [seen[remaining], i]
            seen[v] = i
        return []
s1 = Solution()
print(s1.two_sum([2,5,7,2,3,2],9))