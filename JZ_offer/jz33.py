'''
丑数

做法：动态规划，设置p2,p3,p5三个指针点，比较min([res[p2]*2,res[p3]*3,res[p5]*5])
'''
# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index <= 0:
            return 0
        p2=p3=p5 = 0
        res = [1]
        for i in range(1,index):
            min_num = min([res[p2]*2,res[p3]*3,res[p5]*5])
            res.append(min_num)
            if min_num == res[p2]*2:
                p2 += 1
            if min_num ==res[p3]*3:
                p3 += 1
            if min_num == res[p5]*5:
                p5 += 1
        return res[-1]