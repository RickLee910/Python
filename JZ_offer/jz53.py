# -*- coding: utf-8 -*-
# __author__:song
# 2020/12/3 15:50
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here
        dp = [[False] * (len(pattern)+1) for _ in range(len(s)+1)]
        dp[0][0] = True
        for i in range(1,len(pattern)+1):
            if pattern[i-1] == '*':
                dp[0][i] = dp[0][i-2]
        for i in range(1,len(s)+1):
            for j in range(1,len(pattern)+1):
                if s[i-1] == pattern[j-1] or pattern[j-1] == '.':
                    dp[i][j]=dp[i-1][j-1]
                elif pattern[j-1] == '*':
                    if s[i-1] != pattern[j-2] and pattern[j-2] !='.':
                        dp[i][j] = dp[i][j-2]
                    else:
                        dp[i][j] = dp[i-1][j-2] | dp[i-1][j]
                else:
                    dp[i][j] = False
        return dp[len(s)][len(pattern)]
s = Solution()
a = ''
b= '.*'
print(s.match(a,b))