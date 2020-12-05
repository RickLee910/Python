'''
从上往下打印出二叉树的每个节点，同层节点从左至右打印。

做法：BFS
'''

class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            for i in range(len(stack)):
                node = stack.pop(0)
                res.append(node.val)
                if node.left:stack.append(node.left)
                if node.right:stack.append(node.right)
        return res