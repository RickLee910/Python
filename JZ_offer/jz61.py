# -*- coding: utf-8 -*-
# __author__:song
# 2020/12/3 22:10
'''
按行打印二叉树
BFS
'''
class Solution:
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        stack = [pRoot]
        res = []
        buf = []
        while stack:
            for i in range(len(stack)):
                temp = stack.pop(0)
                buf.append(temp.val)
                if temp.left: stack.append(temp.left)
                if temp.right: stack.append(temp.right)
            res.append(buf)
            buf = []
        return res