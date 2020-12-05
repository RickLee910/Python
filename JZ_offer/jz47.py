# -*- coding: utf-8 -*-
# __author__:song
# 2020/12/2 13:48
'''
f(x) = (f(x-1) + m) % n
'''
class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if n <= 0:
            return False
        index = 0
        for i in range(2,n+1):
            index = (index + m) % i
        return index
s = Solution()
print(s.LastRemaining_Solution(5,3))