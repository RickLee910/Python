class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        temp = []
        for i in lists:
            while i:
                temp.append(i.val)
                i = i.next
        temp.sort()
        ans = ListNode()
        pre = ans
        for i in temp:
            ans.next = ListNode(i)
            ans = ans.next
        return pre.next