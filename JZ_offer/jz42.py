# -*- coding: utf-8 -*-
# __author__:song
# 2020/12/2 0:53
'''
双指针
'''
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        if len(array) < 2:
            return []
        i,j = 0,len(array)-1
        min_mult = float('inf')
        res = []
        while i < j:
            if array[i] + array[j] == tsum:
                if array[i] * array[j] < min_mult:
                    res = [array[i],array[j]]
                    min_mult = array[i] * array[j]
                i += 1
                j -= 1
            elif array[i] + array[j] > tsum:
                j -= 1
            else:
                i += 1

        return res
s = Solution()
a = [1,2,4,7,11,15]
print(s.FindNumbersWithSum(a,15))