# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        hashcycle = False
        p, p2 = head, head

        while p2.next != None and p2.next.next != None:
            p = p.next
            p2 = p2.next.next
            if p == p2:
                hashcycle = True
                break

        if hashcycle:
            temp = head

            while temp != p:
                p = p.next
                temp = temp.next

            return temp
        else:
            return None