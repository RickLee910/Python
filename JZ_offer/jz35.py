from typing import List
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        n = len(nums)
        tmp = [0] * n
        def mergeSort(nums,temp,l,r):
            if l >= r:
                return 0
            mid = l + (r-l)//2
            count = mergeSort(nums,temp,l,mid) + mergeSort(nums,temp,mid+1,r)
            i,j,pos = l,mid+1,l
            #在额外列表里存储归并排序
            while i <= mid and j <= r:
                if nums[i] <= nums[j]:
                    temp[pos] = nums[i]
                    i += 1
                    count += (j-(mid+1))
                else:
                    temp[pos] = nums[j]
                    j += 1
                pos += 1
            #清空比较完的左右二分列表
            for k in range(i, mid+1):
                temp[pos] = nums[k]
                count += j - (mid + 1)
                pos += 1
            for k in range(j,r+1):
                temp[pos] = nums[k]
                pos += 1
            nums[l:r+1] = temp[l:r+1]
            return count %1000000007
        return mergeSort(nums, tmp, 0, n - 1)

s = Solution()
a =[1,2,3,4]
print(s.reversePairs(a))