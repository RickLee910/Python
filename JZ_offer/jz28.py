# -*- coding:utf-8 -*-
'''
数组中出现超过一半的数字
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组
{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。

做法：1.排序,i和i+l的数对比是否相同
2.利用hash记录出现次数
'''
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if len(numbers) == 0:
            return 0
        if len(numbers) == 1:
            return 1
        numbers.sort()
        l = len(numbers) // 2
        for i in range(l):
            if numbers[i] == numbers[i + l]:
                return numbers[i]
        return 0
