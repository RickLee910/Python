# -*- coding: utf-8 -*-
# __author__:song
# 2020/12/3 1:26
'''
把字符串转换成整数
做法：1.ord('2') - ord('0')获得值
2.max(-2 ** 31, min(2 ** 31 - 1, flag * ret)) 防止溢出

'''
class Solution:
    def StrToInt(self, s):
        # write code here
        ls = list(s.strip())
        if not ls: return 0
        flag = -1 if ls[0] == '-' else 1
        if ls[0] in ['+', '-']: del ls[0]
        ret, i = 0, 0
        while i < len(ls):
            if ls[i].isdigit():
                ret = ret * 10 + ord(ls[i]) - ord('0')
                i += 1
            else:
                return 0
        return max(-2 ** 31, min(2 ** 31 - 1, flag * ret)) # 防止溢出