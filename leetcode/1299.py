class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        right_max = -1
        for index in range(len(arr) - 1, -1, -1):
            new_max = max(right_max, arr[index])
            arr[index] = right_max
            right_max = new_max
        return arr