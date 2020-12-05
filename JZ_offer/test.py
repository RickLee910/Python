class Solution:
    def solve_bangbang(self , n , m , k ):
        if m==0:return 1
        dp=[[0 for j in range(m+1)] for i in range(n+1)]
        mod=int(1e9+7)
        for i in range(1,n+1):
            dp[i][1]=1
        for j in range(2,m+1):
            res=0
            for i in range(k+2,n+1):
                res=(res+dp[i-k-1][j-1])%mod
                dp[i][j]=res
        #print(dp)
        res=0
        for i in range(1,n+1):
            res=(res+dp[i][m])%mod
        return res

s = Solution()
print(s.solve_bangbang(5,2,1))