# -*- coding: utf-8 -*-
# __author__:song
# 2020/12/2 13:34
'''
顺子
做法：排序+遍历
'''
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if numbers == []:
            return False
        numbers.sort()
        count = 0
        while numbers[count] == 0:
            count += 1

        if count == 4:
            return True
        for i in range(count, 5):
            if numbers[i] == numbers[i - 1]:
                return False
        return numbers[4] - numbers[count] < 5
