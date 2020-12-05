# -*- coding: utf-8 -*-
# __author__:song
# 2020/12/3 21:38
'''
对称二叉树
做法：递归
'''
class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        def helper(node1,node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            return node1.val == node2.val and helper(node1.left, node2.right) and helper(node1.right, node2.left)
        return helper(pRoot, pRoot)