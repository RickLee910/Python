class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def num(node:ListNode):
            temp = []
            ans = 0
            while node:
                temp.append(node.val)
                node = node.next
            for i in range(len(temp)):
                ans += temp[i] * 10 ** i
            return ans

        res = list(str(num(l1) + num(l2)))
        Node = ListNode(0)
        prior = Node
        for i in res[::-1]:
            Node.val = int(i)
            Node = Node.next
        return prior
s = Solution()
a = [2,4,3]
b = [5,6,4]
print(s.addTwoNumbers(a,b))