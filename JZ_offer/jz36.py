'''
两个链表的第一个公共节点

做法：双指针循环两链表直到p1 =p2

'''
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        if not pHead1 or not pHead2:
            return None
        pre1,pre2 = pHead1, pHead2
        while pHead1 != pHead2:
            pHead1 = pHead1.next
            pHead2 = pHead2.next
            if pHead1 != pHead2:
                if not pHead1:
                    pHead1 = pre2
                if not pHead2:
                    pHead2 = pre1
        return pHead1