'''
输入一个链表，反转链表后，输出新链表的表头。
做法： 设置pre->None, cur->pHead，然后循环知道cur没有，cur->pHead.next,pHead断链指向pre(None),pHead在原链表上向下
pre在新链表上向前
'''

class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        cur = pHead
        pre = None
        while cur:
            cur = pHead.next
            pHead.next = pre
            pre = pHead
            pHead = cur
        return pre