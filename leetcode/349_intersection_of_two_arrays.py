from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        answer_list = []
        large = None
        small = None
        if len(nums1) > len(nums2):
            large =  nums1
            small =  nums2
        elif len(nums2) > len(nums1):
            large =  nums1
            small =  nums2
        else:
            large = nums1
            small = nums2
        
        for key in small:
            if key in large:
                answer_list.append(key)

        return answer_list
