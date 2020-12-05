class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
  
        preorder = []

        def pre(node):
            if not node:
                return
            preorder.append(node)
            pre(node.left)
            pre(node.right)

        pre(root)

        for i in preorder[1:]:
            root.left = None
            root.right = i
            root = root.right