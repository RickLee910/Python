# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        #DFS + dongtai
        # def helper(root,temp):
        #     if not root:
        #         return
        #     if root in temp.keys():
        #         return temp[root]
        #     money = root.val
        #     if root.left:
        #         money += helper(root.left.left, temp) + helper(root.left.right, temp)
        #     if root.right:
        #         money += helper(root.right.left, temp) + helper(root.right.right, temp)
        #     res = max(money, helper(root.left,temp)+helper(root.right,temp))
        #     temp[root] = res
        #     return res
        # temp = {}
        # return helper(root,temp)
        def helper(root):
            if not root:
                return []
            result = [0,0]
            left = [0,0]
            left = helper(root.left)
            right = [0,0]
            right = helper(root.right)
            result[0] = max(left) + max(right)
            result[1] = left[0] + right[0] + root.val
            return result
        return max(helper(root))