# -*- coding: utf-8 -*-
# __author__:song
# 2020/12/3 19:17
'''
删除链表的重复节点
做法：双指针，从头结点的前一个和头结点开始，原表上删除

'''
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        pre = ListNode(0)
        pre.next = pHead
        node, cur = pre, pHead
        while cur:
            if cur.next and cur.val == cur.next.val:
                while cur.next and cur.val == cur.next.val:
                    cur = cur.next
                cur = cur.next
                node.next = cur
            else:
                node = cur
                cur = cur.next
        return pre.next
