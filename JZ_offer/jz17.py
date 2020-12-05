'''
查看树的子结构
输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）

做法：递归dfs(pRoot1, pRoot2) or dfs(pRoot1.left, pRoot2) or dfs(pRoot1.right, pRoot2)

'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if not pRoot1 or not pRoot2:
            return False

        def dfs(node1, node2):
            if not node2:
                return True
            if not node1:
                return False
            return node1.val == node2.val and dfs(node1.left, node2.left) and dfs(node1.right, node2.right)

        return dfs(pRoot1, pRoot2) or dfs(pRoot1.left, pRoot2) or dfs(pRoot1.right, pRoot2)

t = TreeNode(8)
t.left = TreeNode(8)
t.left.left = TreeNode(9)
t.left.left.left = TreeNode(2)
t.left.left.left.left = TreeNode(5)
t1 = TreeNode(8)
t1.left = TreeNode(9)
t1.left.left = TreeNode(2)
s = Solution()
t.left,t.right = t.right,t.left
print(t)