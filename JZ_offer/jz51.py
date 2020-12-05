# -*- coding: utf-8 -*-
# __author__:song
# 2020/12/3 15:37
'''
数组中的重复数字
做法：hash
'''
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        hash = {}
        for i in numbers:
            if i in hash:
                duplication[0] = i
                return True
            else:
                hash[i] = 1
        return False