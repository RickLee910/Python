# -*- coding: utf-8 -*-
# __author__:song
# 2020/12/3 0:31
'''
不用符号求加法
做法：背下来
'''
class Solution:
    def Add(self, num1, num2):
        # write code here
        x = 0xffffffff
        num1,num2 = num1 & x,num2&x
        while num2 != 0:
            num1,num2 = num1^num2,(num1&num2)<<1 & x
        return num1 if num1 < 0x7fffffff else ~(num1 ^ x)
s = Solution()
a = 5
b = -3
print(s.Add(a,b))