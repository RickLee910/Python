
'''
输入一颗二叉树的根节点和一个整数，按字典序打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。

做法：dfs(root,res,cur):
注意此题是到叶子结点，所以好做一些

'''
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        result = []
        if root == None:
            return result
        def dfs(root,res,cur):
            if not root.left and not root.right and sum(cur) == expectNumber:
                res.append(cur)
            if root.left:
                dfs(root.left,res,cur + [root.left.val])
            if root.right:
                dfs(root.right,res,cur + [root.right.val])
        dfs(root, result, [root.val])
        return result