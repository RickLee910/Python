# -*- coding: utf-8 -*-
# __author__:song
# 2020/12/4 17:41
# -*- coding:utf-8 -*-
'''
剪绳子
做法：数学技巧，围绕3展开
'''
class Solution:
    def cutRope(self, number):
        # write code here
        if number == 2:
            return 2
        elif number == 3:
            return 3
        else:
            if number % 3 == 0:
                return 3 ** (number // 3)
            elif number % 3 == 1:
                return 4 * 3 ** ((number-4) // 3)
            else:
                return 2 * 3 ** ((number-2) // 3)