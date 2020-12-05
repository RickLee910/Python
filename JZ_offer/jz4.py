# -*- coding:utf-8 -*-
'''
题目描述
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。

方法：递归构建树，利用前序遍历找到root点，然后在中序遍历里找到index,划分左右子树的范围，然后递归求解
同理做 后序 + 中序
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder or not postorder:
            return
        root = TreeNode(postorder[-1])
        idx = inorder.index(postorder[-1])
        root.right = self.buildTree(inorder[idx+1:],postorder[idx:-1])
        root.left = self.buildTree(inorder[:idx+1],postorder[:idx])
        return root
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre or not tin:
            return
        root = TreeNode(pre[0])
        idx = tin.index(pre[0])
        root.left = self.reConstructBinaryTree(pre[1:1 + idx], tin[:idx])
        root.right = self.reConstructBinaryTree(pre[1 + idx:], tin[idx + 1:])
        return root
