# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        temp = []
        while head:
            temp.append(head.val)
            head = head.next
        temp.pop(-n)
        ans = ListNode()
        pre = ans
        for i in range(len(temp)):
            ans.next = ListNode(temp[i])
            ans = ans.next

        return pre.next