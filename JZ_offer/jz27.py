'''
字符串的排列
输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,则按字典序打印出由
字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。

做法：dfs思想，参数包含当前的list和一个temp string,利用切片s[:i]+s[i+1:]和path + s[i]的拼接在循环中递归调用函数
'''
class Solution:
    def Permutation(self, ss):
        # write code here
        self.res = []
        n = len(ss)
        if ss == '':
            return []
        def backtrack(s, path):
            if not s:
                self.res.append(path)
            seen = set()
            for i in range(len(s)):
                if s[i] in seen: continue
                seen.add(s[i])
                backtrack(s[:i]+s[i+1:], path + s[i])

        backtrack(ss, "")
        return self.res