# -*- coding:utf-8 -*-
'''
请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。

注意是 每个空格，用str.split()不能很好处理
for循环解决
'''
class Solution:
    # s 源字符串
    def replaceSpace(self, s:str):
        res = ''
        temp = list(s)
        for i in temp:
            if i == ' ':
                res += '%20'
            else:
                res += i
        return res


s = Solution()
a = '  We are happy '
print(s.replaceSpace(a))