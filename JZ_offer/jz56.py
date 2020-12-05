# -*- coding: utf-8 -*-
# __author__:song
# 2020/12/3 19:16
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
链表环的入口节点
做法：快慢指针，然后重设慢指针知道重合


'''
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        i,j = pHead, pHead
        while i and i.next:
            i = i.next.next
            j = j.next
            if i == j:
                j2 = pHead
                while j2 != j:
                    j = j.next
                    j2 = j2.next
                return j2
        return None