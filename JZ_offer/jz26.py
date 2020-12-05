'''
二叉搜索树的双向链表
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。

做法：从右子树开始向左遍历，行成的双向链表是从末端向左行程的
'''

class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        self.pre = None

        def helper(node):
            if not node:
                return
            helper(node.right)
            if self.pre:
                node.right = self.pre
                self.pre.left = node
            self.pre = node
            helper(node.left)
            

        helper(pRootOfTree)
        return self.pre