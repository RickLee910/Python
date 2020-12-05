# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
    def push(self, node):
        # write code here

        self.stack.append(node)
    def pop(self):
        # return xx
        return self.pop(0)