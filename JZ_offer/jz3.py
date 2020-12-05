# -*- coding:utf-8 -*-


'''
输入一个链表，按链表从尾到头的顺序返回一个ArrayList。
利用队列从左端输入appendleft()
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
import collections

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        temp = collections.deque()
        while listNode:
            temp.appendleft(listNode.val)
            listNode = listNode.next
        return temp