# -*- coding: utf-8 -*-
# __author__:song
# 2020/12/2 12:36
'''
字符串的拼接
'''
class Solution:
    def ReverseSentence(self, s:str):
        # write code here
        temp = ''
        temp_s = ''
        res = []
        if s == '':
            return ''
        for i in s:
            if i.isspace():
                temp += ' '
                if temp_s != '':
                    res.append(temp_s)
                temp_s = ''
            else:
                if temp != '':
                    res.append(temp)
                temp = ''
                temp_s += i
        if temp != '':
            res.append(temp)
        if temp_s != '':
            res.append(temp_s)
        return ''.join(res[::-1])

if __name__ == "__main__":
    s = Solution()
    a = "  student . a am I  "
    print(s.ReverseSentence(a))