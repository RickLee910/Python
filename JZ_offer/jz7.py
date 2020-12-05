# -*- coding:utf-8 -*-
'''
斐波那契数列
'''
class Solution:
    def Fibonacci(self, n):
        # write code here
        # a = 0
        # b = 1
        # if n == 0 or n == 1:
        #     return n
        # for i in range(n-1):
        #     a,b = b,a+b
        # return b
        if n < 2:
            return 1
        return self.Fibonacci(n-1)+self.Fibonacci(n-2)
s = Solution()
for i in range(10):
    print(s.Fibonacci(i))