# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        res = base ** exponent
        return float(res)
s = Solution()
a = 2
b = 3
print(s.Power(a,b))