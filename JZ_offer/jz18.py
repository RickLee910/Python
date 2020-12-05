'''
操作给定的二叉树，将其变换为源二叉树的镜像。
做法：简单的递归左右子树，交换左右子树的值
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        def swap(node):
            if not node:
                return

            swap(node.left)
            swap(node.right)
            node.left, node.right = node.right, node.left

        swap(root)
        return root
t = TreeNode(8)
t.left = TreeNode(8)
t.left.left = TreeNode(9)
t.left.left.left = TreeNode(2)
t.left.left.left.left = TreeNode(5)
s = Solution()
print(s.Mirror(t))