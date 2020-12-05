class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        if m * n == 0:
            return m+n
        dp = [[0]*(n+1) for i in range(m+1)]
        for i in range(n+1):
            dp[0][i] = i
        for j in range(m+1):
            dp[j][0] = j
        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i -1] == word2[j-1]:
                    dp[i][j] = 1+min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1] - 1)
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
        return dp[-1][-1]
s = Solution()
a = 'horse'
b='ros'
print(s.minDistance(a,b))