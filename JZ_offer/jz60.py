# -*- coding: utf-8 -*-
# __author__:song
# 2020/12/3 21:59
'''
按之字形顺序打印二叉树
BFS
'''


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        stack = [pRoot]
        res = []
        buf = []
        flag = 0
        while stack:
            if flag == 1:
                for i in range(len(stack)):
                    temp = stack.pop(0)
                    buf.append(temp.val)
                    if temp.left: stack.append(temp.left)
                    if temp.right: stack.append(temp.right)
                buf.reverse()
                res.append(buf)

                flag = 0
            else:
                for i in range(len(stack)):
                    temp = stack.pop(0)
                    buf.append(temp.val)
                    if temp.left: stack.append(temp.left)
                    if temp.right: stack.append(temp.right)
                res.append(buf)
                flag = 1
            buf = []
        return res
