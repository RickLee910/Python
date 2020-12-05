'''
第一个只出现一次的字符

做法：利用hash表记录位置
'''

class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if s == '':
            return -1
        if len(s) == 1:
            return 0
        temp = {}
        visited = []
        for i in range(len(s)):
            if s[i] not in visited:
                if s[i] in temp:
                    visited.append(s[i])
                    temp.pop(s[i])
                else:
                    temp[s[i]] = i
        return min(temp.values())