class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        temp =  sorted(nums1 + nums2)
        if len(temp) % 2== 1:
            return temp[len(temp) // 2]
        else:
            return (temp[len(temp) // 2] + temp[(len(temp) // 2 - 1)]) / 2