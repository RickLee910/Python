class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        l_s = len(s)

        dp = [False]* (l_s+1)
        dp[0] = True


        for i in range(l_s+1):
            for j in range(0,i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[l_s]
s = Solution()
a = "abcd"
b = ["a","abc","b","cd"]
print(s.wordBreak(a,b))