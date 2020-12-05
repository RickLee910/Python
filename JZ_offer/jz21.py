# -*- coding:utf-8 -*-
'''
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。
假设压入栈的所有数字均不相等。例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该
压栈序列对应的一个弹出序列，但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两
个序列的长度是相等的）

做法：压栈后的数组和出栈做实施比较，有相同时就pop，如果最后循环结束时压栈没有清空，则False
'''
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        stack = []
        j = 0
        for i in range(len(pushV)):
            stack.append(pushV[i])
            while stack[-1] == popV[j]:
                stack.pop()
                j += 1
                if stack == []:
                    break
        if j != len(popV):
            return False
        else:
            return True


s = Solution()
a = [1,2,3,4,5]
b = [4,3,5,1,2]
print(s.IsPopOrder(a,b))