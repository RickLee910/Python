# -*- coding: utf-8 -*-
# __author__:song
# 2020/12/3 22:12\
# -*- coding:utf-8 -*-
'''
序列化二叉树和恢复二叉树

'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.flag = -1

    def Serialize(self, root):
        # write code here
        if not root:
            return '#,'
        return str(root.val) + ',' + self.Serialize(root.left) + self.Serialize(root.right)

    def Deserialize(self, s):
        # write code here
        self.flag += 1
        l = s.split(',')

        if self.flag >= len(s):
            return None
        root = None

        if l[self.flag] != '#':
            root = TreeNode(int(l[self.flag]))
            root.left = self.Deserialize(s)
            root.right = self.Deserialize(s)
        return root

        return depreorder(s, 0)
t = TreeNode(8)
t.left = TreeNode(6)
t.right = TreeNode(10)
t.left.left = TreeNode(5)
s = Solution()
print(s.Deserialize(s.Serialize(t)))