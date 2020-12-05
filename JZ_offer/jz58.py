# -*- coding: utf-8 -*-
# __author__:song
# 2020/12/3 19:47
'''
二叉树的下一个节点
做法：1.笔试：中序遍历递归
2.面试，分类讨论，画图理解
'''


class Solution:
    def GetNext(self, pNode):
        # write code here
        self.temp = []

        def inorder(node):
            if not node:
                return 0
            inorder(node.left)
            self.temp.append(node)
            inorder(node.right)

        root, temp = None, pNode
        while temp:
            root = temp
            temp = temp.next
        inorder(root)
        for i in range(len(self.temp)):
            if self.temp[i] == pNode and i + 1 != len(self.temp):
                return self.temp[i + 1]
        return None

