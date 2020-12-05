# -*- coding: utf-8 -*-
# __author__:song
# 2020/12/3 18:51
class Solution:
    # 返回对应char
    def __init__(self):
        self.s=''
    def FirstAppearingOnce(self):
        # write code here
        res=[]
        for i in self.s:
            if i in res:
                res.remove(i)
            else:
                res.append(i)
        return res[0] if res else "#"
    def Insert(self, char):
        # write code here
        self.s+=char