# -*- coding:utf-8 -*-
'''
和为S的连续正数序列
做法：滑动窗口 + 快慢指针调节滑动窗口
'''
# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        if tsum <= 2:
            return []
        i,j = 1,2
        res = []
        temp = 3
        while i < j:
            if temp == tsum:
                temp1 = []
                for k in range(i,j+1):
                    temp1.append(k)
                temp += j + 1 - i
                i += 1
                j += 1

                res.append(temp1)
            elif temp > tsum:
                temp -= i
                i += 1

            else:
                j += 1
                temp += j
        return res
s = Solution()
a = 100
print(s.FindContinuousSequence(a))