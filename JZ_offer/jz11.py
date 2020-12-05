# -*- coding:utf-8 -*-
'''
输入一个整数，输出该数32位二进制表示中1的个数。其中负数用补码表示。

做法： n =  n & (n-1) 进行循环计数
'''
class Solution:
    def NumberOf1(self, n):
        # write code here
        count = 0
        if n < 0:
            n = n & 0xffffffff #获得一个数在计算机中的二进制表示形式
        while n:
                count += 1
                n =  n & (n-1)
        return count

s = Solution()
a = -2048
print(s.NumberOf1(a))