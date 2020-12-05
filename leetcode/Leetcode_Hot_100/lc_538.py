# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            nonlocal total
            if node:
                dfs(node.right)
                total += node.val
                node.val = total
                dfs(node.left)

        pre = root
        total = 0
        dfs(root)
        return pre
t = TreeNode(4)
t.right = TreeNode(6)
t.right.left = TreeNode(5)
t.right.right = TreeNode(7)
t.right.right.right = TreeNode(8)
s = Solution()
print(s.convertBST(t))
