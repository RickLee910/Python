# -*- coding:utf-8 -*-
'''
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？

比如n=3时，2*3的矩形块有3种覆盖方法：

做法：同斐波那契数列
'''
class Solution:
    def rectCover(self, number):
        # write code here
        if number <2:
            return number
        dp = [0] * (number+1)
        dp[0],dp[1] = 1,1
        for i in range(2,number+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[number]