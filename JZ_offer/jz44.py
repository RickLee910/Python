# -*- coding: utf-8 -*-
# __author__:song
# 2020/12/2 12:32
'''
字符串的切片
'''
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        if s == '':
            return ''
        mid = n % (len(s))
        return s[mid:]+ s[:mid]