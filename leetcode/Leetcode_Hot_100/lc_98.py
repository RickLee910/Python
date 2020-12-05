
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        stack = [root]
        ans = []
        if root == None:
            return ans
        while stack:
            temp = []
            for i in range(len(stack)):
                flag = stack.pop(0)
                if flag.left: stack.append(flag.left)
                if flag.right: stack.append(flag.right)
                temp.append(flag.val)
            ans.append(temp)
        return ans