'''

输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则返回true,否则返回false。假设输入的数组的任意两个数字都互不相同。

做法：递归，helper(List,start,end)
利用后续遍历最后一个是根节点的特性，再加上二叉搜索树左小右大的特性，递归左子树列表和右子树列表

'''

class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        def helper(List,start,root):
            if start >= root:
                return True
            #判断右子树开始节点
            for i in range(start,root+1):
                if List[i] >= List[root]:
                    break
            #由于前面从左子树开始筛选，所以左侧都是小于List[root]的，仅需比较右侧到root的值
            for j in range(i,root):
                if List[j] < List[root]:
                    return False
            return helper(List, start, i-1)  and helper(List, i, root-1)
        if len(sequence) == 0:
            return False
        return helper(sequence,0,len(sequence)-1)
s = Solution()
a = [4,8,6,12,16,14,10]
print(s.VerifySquenceOfBST(a))