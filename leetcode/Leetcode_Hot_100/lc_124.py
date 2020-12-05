# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.res = root.val
        def maxvalue(node):
            if not node:
                return 0
            leftvalue = maxvalue(node.left)
            rightvalue = maxvalue(node.right)

            value1 = node.val
            value2 = node.val + leftvalue
            value3 = node.val + rightvalue
            value4 = node.val + leftvalue + rightvalue

            maxValue = max(value1,value2,value3,value4)
            self.res = max(maxValue,self.res)
            return max([value1,value2,value3])
        maxvalue(root)
        return self.res