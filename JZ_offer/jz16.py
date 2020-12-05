# -*- coding:utf-8 -*-
'''
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。

做法：迭代，递归
TIPS：注意要先赋予空指针.next链表节点，否则无法node = node.next
递归方法很巧妙，借助图像来进行理解
1->
    2->
        3->
            4->
                5->
                pHead1 = None
                return pHead2(6->)
                5->6->
            4->5->6->
        3->4->5->6->
    2->3->4->5->6->
1->2->3->4->5->6->
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        # if not pHead1:
        #     return pHead2
        # if not pHead2:
        #     return pHead1
        # node = ListNode(None)
        # pre = node
        # while pHead1 and pHead2:
        #     if pHead1.val <= pHead2.val:
        #         node.next = ListNode(pHead1.val)
        #         node = node.next
        #         pHead1 = pHead1.next
        #     else:
        #         node.next = ListNode(pHead2.val)
        #         node = node.next
        #         pHead2 = pHead2.next
        # if pHead1:
        #     node.next = pHead1
        # elif pHead2:
        #     node.next = pHead2
        # return pre.next
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1
        if pHead1.val <= pHead2.val:
            pHead1.next =self.Merge(pHead1.next,pHead2)
            return pHead1
        else:
            pHead2.next = self.Merge(pHead1,pHead2.next)
            return pHead2

l1 = ListNode(1)
l1.next = ListNode(3)
l1.next.next = ListNode(5)
l2 = ListNode(2)
l2.next = ListNode(4)
l2.next.next = ListNode(6)
s = Solution()
print(s.Merge(l1,l2))