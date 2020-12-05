# -*- coding: utf-8 -*-
# __author__:song
# 2020/12/3 23:05
'''
二叉搜索树的第k个节点
做法：1.简单：中序存储到list中
2.中序递归return,
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        self.n = 0
        def inorder(node):
            if node:
                temp = inorder(node.left)
                if temp: #防止覆盖，一旦传回node非空，直接return回去
                    return temp
                self.n += 1
                if self.n == k:
                    return node
                temp = inorder(node.right)
                if temp:
                    return temp


        return inorder(pRoot)

t = TreeNode(8)
t.left = TreeNode(6)
t.right = TreeNode(10)
t.left.left = TreeNode(5)
s = Solution()
print(s.KthNode(t,1))