# -*- coding:utf-8 -*-
'''
把数组排成最小的数

做法：转换为string数组，然后利用冒泡排序思想，每迭代一次确定一位最终位置

'''

class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        for i in range(len(numbers)):
            numbers[i] = str(numbers[i])
        for i in range(len(numbers)):
            for j in range(i+1,len(numbers)):
                if numbers[j] + numbers[i] < numbers[i] + numbers[j]:
                    numbers[i],numbers[j] = numbers[j],numbers[i]
        return ''.join(numbers)
s =  Solution()
a = [5,2,6,3,21]
print(s.PrintMinNumber(a))