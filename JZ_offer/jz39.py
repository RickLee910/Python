'''
判断是否为平衡二叉树
做法：从下到上递归
'''

class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        #DFS
        def helper(node):
            if not node:
                return 0
            left = helper(node.left)
            if left == -1:
                return -1
            right = helper(node.right)
            if right == -1:
                return -1
            if left - right < -1 or left - right > 1:
                return -1
            else:
                return 1 + (left if left > right else right)
        return helper(pRoot) != -1