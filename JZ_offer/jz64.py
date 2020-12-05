# -*- coding: utf-8 -*-
# __author__:song
# 2020/12/4 0:18
'''
数据流中的中位数
利用heapq，注意导入小顶堆的时候用负数
'''
from heapq import *

class MedianFinder:
    def __init__(self):
        self.A = [] # 小顶堆，保存较大的一半
        self.B = [] # 大顶堆，保存较小的一半

    def addNum(self, num: int) -> None:
        if len(self.A) != len(self.B):
            heappush(self.B, -heappushpop(self.A, num))
        else:
            heappush(self.A, -heappushpop(self.B, -num))

    def findMedian(self) -> float:
        return self.A[0] if len(self.A) != len(self.B) else (self.A[0] - self.B[0]) / 2.0
s = MedianFinder()
a =[5,2,3,4,1,6,7,0,8]

for i in a:
    s.addNum(i)
    print(s.findMedian() )