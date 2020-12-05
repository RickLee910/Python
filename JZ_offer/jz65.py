# -*- coding: utf-8 -*-
# __author__:song
# 2020/12/4 12:16
'''
滑动窗口的最大值
做法：1.简单：直接遍历，然后max切片的数组
2.高级：利用队列，存储递减序列，保持队列头是当前最大值，滑动出去的值和头对上则popleft
'''
# -*- coding:utf-8 -*-
from collections import deque
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        if size == 0 or size > len(num):
            return []
        res = []
        d = deque()
        for i in range(size):
            if not d or num[i] <= d[-1]:
                d.append(num[i])
            else:
                while d:
                    if num[i] > d[-1]:
                        d.pop()
                    else:
                        break
                d.append(num[i])
        res.append(d[0])
        for i in range(size,len(num)):
            if d[0] == num[i-size]:
                d.popleft()
            while d:
                if num[i] > d[-1]:
                    d.pop()
                else:
                    break
            d.append(num[i])
            res.append(d[0])
        return res
s = Solution()
a = [16,14,12,10,8,6,4]
print(s.maxInWindows(a,5))