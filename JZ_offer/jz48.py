# -*- coding: utf-8 -*-
# __author__:song
# 2020/12/2 18:20
# -*- coding:utf-8 -*-
'''
1+2+3...n
位运算
n > 1 and f(n-1)
'''
class Solution:
    def __init__(self):
        self.res = 0
    def Sum_Solution(self, n):
        # write code here
        n > 1 and self.Sum_Solution(n-1)
        self.res += n
        return self.res