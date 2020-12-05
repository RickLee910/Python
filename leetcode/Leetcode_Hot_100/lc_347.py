from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #暴力
        # temp = {}
        # res = []
        # out = []
        # def take2(a):
        #     return a[1]
        # for i in nums:
        #     if i in temp.keys():
        #         temp[i] += 1
        #     else:
        #         temp[i] = 1
        # for i in temp.keys():
        #     res.append([i,temp[i]])
        # res.sort(key=take2)
        # for i in range(k):
        #     out.append(res[-i-1][0])
        # return out
        #暴力优化内存
        # temp = {}
        # res = []
        #
        #
        # def take2(a):
        #     return a[1]
        #
        # for i in nums:
        #     if i in temp.keys():
        #         temp[i] += 1
        #     else:
        #         temp[i] = 1
        # for i in temp.keys():
        #     res.append([i, temp[i]])
        # res.sort(key=take2)
        #
        # return list(res[-i-1][0] for i in range(k))
        #
        #建立大顶堆后堆排序 大到小
        def siftdown(nums,e,begin,end):#e:输入时的nums[i]
            i,j = begin,begin*2+1
            while j < end:
                if j+1 < end and nums[j+1][1] > nums[j][1]:#维护最大值，更新j
                    j+=1
                if nums[j][1] < e:
                    break
                nums[i],nums[j]=nums[j],nums[i]
                i, j = j, j * 2 + 1
        temp = {}
        for i in nums:
            if i in temp.keys():
                temp[i] += 1
            else:
                temp[i] = 1
        num = list(temp.items())
        #初始化 无序 建立大顶堆
        for i in range(len(num)//2-1,-1,-1):
            siftdown(num,num[i][1],i,len(num))
        #排序大顶堆 大-》小 交换头尾节点，重置大跟堆
        for i in range(len(num) - 1,0,-1):
            num[0],num[i] = num[i],num[0]
            siftdown(num,num[0][1],0,i)
        res = []
        for i in range(k):
            res.append(num[-i - 1][0])
        return res
s = Solution()
a =  [3,2,5,2,1,6,3,3,12,2]
print(s.topKFrequent(a,2))