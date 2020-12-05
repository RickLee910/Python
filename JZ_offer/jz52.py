# -*- coding: utf-8 -*-
# __author__:song
# 2020/12/3 15:49
'''
构建乘积数组
做法：分为左右列表连乘后再合并2个for
'''


class Solution:
    def multiply(self, A):
        # write code here
        temp = 1
        B = [1] * len(A)
        for i in range(1, len(A)):
            B[i] = B[i - 1] * A[i - 1]
        for i in range(len(A) - 2, -1, -1):
            temp *= A[i + 1]
            B[i] *= temp
        return B
