# -*- coding: utf-8 -*-
# __author__:song
# 2020/12/3 18:15
class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        if len(s) == 0:
            return False
        hash = {'+': 2, '-': 2, 'e': 1, '.': 1}
        if s[0].isdigit() or s[0] in '+-':
            if s[0] in hash:
                hash[s[0]] -= 1
            for i in range(1, len(s)):
                if s[i] not in '+-eE.' and not s[i].isdigit():
                    return False
                if s[i] in 'eE':
                    hash['e'] -= 1
                    if not s[i - 1].isdigit or i + 1 == len(s) or s[i + 1] in 'eE.':
                        return False

                if s[i] == '.':
                    hash['.'] -= 1
                    if hash['.'] == hash['e'] == 0:
                        return False
                    if i + 1 == len(s) or s[i - 1] in 'eE.' or s[i + 1] in hash:
                        return False
                if s[i] in '+-':
                    hash[s[i]] -= 1
                    if s[i - 1] == '.' or i + 1 == len(s) or s[i + 1] in 'eE.' or i == 1:
                        return False
                    if s[i - 1].isdigit() and s[i + 1].isdigit():
                        return False
                for j in hash:
                    if hash[j] < 0:
                        return False
        else:
            return False
        return True
