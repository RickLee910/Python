# -*- coding:utf-8 -*-
'''
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。

做法：1.暴力法，辅助数组
2.原地反向冒泡替换

'''
class Solution:
    def reOrderArray(self, array):
        # # write code here
        # temp1 = []
        # temp2 = []
        # for i in array:
        #     if i % 2 == 1:
        #         temp1.append(i)
        #     else:
        #         temp2.append(i)
        # return temp1 + temp2
        i,j = 0, 0
        for x in range(len(array)):
            if array[x] % 2 == 1:
                if i != j:
                    for n in range(j,i,-1):
                        array[n-1],array[n] =array[n],array[n-1]
                i += 1
                j += 1
            else:
                j += 1
        return array
s = Solution()
a = [1,56,23,2,31,2,3,3]
print(s.reOrderArray(a))