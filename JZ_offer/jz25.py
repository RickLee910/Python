# -*- coding:utf-8 -*-
'''
复杂链表的复制
输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针random指向一
个随机节点），请对此链表进行深拷贝，并返回拷贝后的头结点。（注意，输出结果中请不要返回参数中的节点引
用，否则判题程序会直接返回空）

做法：DFS，BFS，迭代
精髓：创建新结点，构建新链表。设置visited hash dictionary然后重新构建一条链表
'''

class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        #DFS
        # def dfs(head):
        #     if not head:
        #         return
        #     if head in visited:
        #         return visited[head]
        #
        #     copy = RandomListNode(head.label)
        #     visited[head] = copy
        #     copy.next = dfs(head.next)
        #     copy.random = dfs(head.random)
        #     return copy
        #
        # visited = {}
        # return dfs(pHead)
        #BFS
        if not pHead:
            return pHead
        stack = [pHead]
        visited = {}
        res = RandomListNode(pHead.label)
        visited[pHead] = res
        while stack:
            temp = stack.pop(0)
            if temp.next and temp.next not in visited:
                stack.append(temp.next)
                visited[temp.next] = RandomListNode(temp.next.label)
            if temp.random and temp.random not in visited:
                stack.append(temp.random)
                visited[temp.random] = RandomListNode(temp.random.label)
            # 这里一定要用dict.get(item),当item不在visited里面时，return None,
            # 直接使用dict[item]会报错if item not in dict
            visited[temp].next = visited.get(temp.next)
            visited[temp].random = visited.get(temp.random)
        return res

l = RandomListNode(3)
l.next = RandomListNode(4)
l.random = None
l.next.next = RandomListNode(5)
l.next.random = l
l.next.next.next = l.random
l.next.next.random = l.random
s = Solution()
print(s.Clone(l))