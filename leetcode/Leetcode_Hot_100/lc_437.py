class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        # dfs
        # def dfs(dp,node):
        #
        #     if not node:
        #         return
        #     dp.append(node.val)
        #     for j in range(len(dp)):
        #         if j < len(dp) - 1:
        #             dp[j] += dp[-1]
        #         if dp[j] == sum:
        #             self.count += 1
        #     dfs(dp, node.left)
        #
        #     dfs(dp, node.right)
        #     temp = dp.pop()
        #     for j in range(len(dp)):
        #         dp[j] -= temp
        # dp = []
        # self.count = 0
        # dfs(dp,root)
        # return self.count

        #dfs优化版
        def dfs(node,dp):
            if not node:
                return 0
            dp = [num + node.val for num in dp]
            dp.append(node.val)
            count = 0
            for i in dp:
                if i == sum:
                    count += 1
            left = dfs(node.left,dp)
            right = dfs(node.right, dp)
            return count + left + right
        return dfs(root,[])
t = TreeNode(10)
root = t
t.left = TreeNode(5)
t.right = TreeNode(-3)
t.right.right = TreeNode(11)
t=t.left
t.left=TreeNode(3)
t.right = TreeNode(2)
t.right.right = TreeNode(1)
t.left.left = TreeNode(3)
t.left.right = TreeNode(-2)
s = Solution()
print(s.pathSum(root,8))
