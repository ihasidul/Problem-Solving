class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        trackers = [0] * 101
        for num in nums:
            trackers[num] += 1
        accumulation = 0
        for i in range(len(trackers)):
            prev = trackers[i]
            trackers[i] = accumulation 
            accumulation += prev
        return [trackers[num] for num in  nums]
