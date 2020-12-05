'''
输入一个链表，输出该链表中倒数第k个结点。

做法：快慢指针
TIPS:注意特殊情况取值范围，return

'''
class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        j = head
        if not head:
            return head
        if k <= 0:
            return
        for i in range(k-1):
            j = j.next
            if not j:
                return j
        while j.next:
            j = j.next
            head = head.next
        return head