class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        def adjustdown(elem,e,begin,end):
            i,j = begin,begin*2 + 1
            while j < end:
                if j+1 < end and elem[j] > elem[j+1]:
                    j += 1
                if e < elem[j]:
                    break
                elem[i],elem[j] = elem[j],elem[i]
                i, j = j, j * 2 + 1
            elem[i] = e

        end = len(nums)
        for i in range(end//2-1,-1,-1):
            adjustdown(nums,nums[i],i,end)
        for i in range(end-1,0,-1):
            e = nums[i]
            nums[i] = nums[0]
            adjustdown(nums,e,0,i)
        return nums[k-1]
s = Solution()
a = [3,2,3,1,2,4,5,5,6]
print(s.findKthLargest(a,5))