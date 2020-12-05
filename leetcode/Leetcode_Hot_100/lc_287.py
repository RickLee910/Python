from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        def maxheap(elem,e,begin,end):
            i,j = begin,begin*2+1
            while j < end:
                if j + 1 < end and elem[j] > elem[j+1]:
                    j+=1
                if e < elem[j]:
                    break
                elem[i],elem[j] = elem[j],elem[i]
                i,j = j, j*2+1
            elem[i] = e
        for i in range(len(nums) // 2 - 1,-1,-1):
            maxheap(nums,nums[i],i,len(nums))
        for i in range(len(nums)-1,0,-1):
            e = nums[i]
            nums[i] = nums[0]
            maxheap(nums,e,0,i)
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return nums[i]
s = Solution()
a = [4,6,8,5,9,9]
print(s.findDuplicate(a))