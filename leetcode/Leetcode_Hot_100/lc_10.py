
class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        s = ' ' + s
        p = ' ' + p
        m, n = len(s), len(p)
        f = [[False] * (n + 1) for _ in range(m + 1)]
        f[0][0] = True
        for i in range(1,m + 1):
            for j in range(1, n + 1):
                if p[j -1] == s[i - 1] or p[j - 1] == '.':
                    f[i][j] = f[i - 1][j - 1]
                elif p[j - 1] == '*':#p[j] != s[i]
                    if p[j-2] != s[i - 1] and p[j-2] !='.':
                        f[i][j] = f[i][j - 2]
                    else:
                        f[i][j] = f[i][j - 1] | f[i][j - 2] | f[i - 1][j]
        return f[m][n]

s = Solution()
a = "ab"
b = ".*c"
print(s.isMatch(a,b))