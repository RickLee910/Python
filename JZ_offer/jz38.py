# -*- coding:utf-8 -*-
'''
二叉树深度

做法：DFS，BFS
TIPS：DFS时depth初始值为1

'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import collections
class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        #BFS
        # stack = collections.deque([pRoot])
        # count = 0
        # while stack:
        #     for i in range(len(stack)):
        #         temp = stack.popleft()
        #         if temp.left:
        #             stack.append(temp.left)
        #         if temp.right:
        #             stack.append(temp.right)
        #     count += 1
        # return count
        #DFS
        self.maxcount = 0

        def dfs(node, depth):
            if not node:
                return 0

            dfs(node.left, depth + 1)
            self.maxcount = max(self.maxcount, depth)
            dfs(node.right, depth + 1)
            self.maxcount = max(self.maxcount, depth)

        dfs(pRoot, 1)
        return self.maxcount
s = Solution()
t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(3)
t.left.right = TreeNode(4)
t.left.right.left = TreeNode(5)
print(s.TreeDepth(t))