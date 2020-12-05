# -*- coding:utf-8 -*-
"""
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，
每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一
个整数，判断数组中是否含有该整数。

输入：7, [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
输出：True
"""

#从右上角开始查找，根据性质可以从右上只遍历左侧和下面的数，大于target->下移 小于target->左移

# class Solution:
#     # array 二维列表
#     def Find(self, target, array):
#         # write code here
#         i,j = 0,len(array[0])-1
#         while i < len(array) and j >= 0:
#             if array[i][j] > target:
#                 j -= 1
#             elif array[i][j] < target:
#                 i += 1
#             else:
#                 return True
#         return False
#
#利用二分查找
#循环对每一行进行二分查找
class Solution:
    # array 二维列表
    def Find(self, target, array):
        if not array:
            return False
        for i in range(len(array)):
            if array[i][0] <= target <= array[i][-1]:
                l = 0
                r = len(array[0])-1
                while l <= r:
                    mid = l + (r - l) // 2
                    if array[i][mid] == target:
                        return True
                    elif array[i][mid] < target:
                        l = mid+1
                    else:
                        r = mid -1
        return False
s = Solution()
a = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
print(s.Find(7,a))