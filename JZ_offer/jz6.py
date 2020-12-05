# -*- coding:utf-8 -*-
'''
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。

二分查找，把 右边界当成target 和 mid值 比较
不能使用左边界当target
'''
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if rotateArray == []:
            return 0
        l,r = 0,len(rotateArray)-1
        while l <r:
            mid = l + (r-l)//2
            if rotateArray[mid] < rotateArray[r]:
                r = mid
            elif rotateArray[mid] > rotateArray[r]:
                l = mid+1
            else:
                r -= 1
        return rotateArray[l]
s = Solution()
a = [4,5,6,2,3,4]
print(s.minNumberInRotateArray(a))