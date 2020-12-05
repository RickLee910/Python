# -*- coding:utf-8 -*-
'''
定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。
做法：维护一个动态队列，对应栈里有几个值时对应多少的最小值
'''
class Solution:
    def __init__(self):
        self.stack = []
        self.minN = float('inf')
        self.notbook = []
    def push(self, node):
        # write code here
        self.stack.append(node)
        self.minN = min(node,self.minN)
        self.notbook.append(self.minN)
    def pop(self):
        # write code here
        self.stack.pop()
        self.notbook.pop()
    def top(self):
        # write code here
        return self.stack[-1]
    def min(self):
        # write code here
        return self.notbook[-1]
s = Solution()
s.push(3)
print(s.min())