class Solution:

    def longestPalindrome(self, s: str) -> str:
        dp = [[False]  * len(s) for i in range(len(s))]
        ans = ''
        for l in range(len(s)):
            for i in range(len(s)):
                j = i + l
                if j >= len(s):
                    break
                if l == 0:
                    dp[i][j] = True
                elif l == 1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (s[i] == s[j] and dp[i+1][j-1] ==True)
                if dp[i][j]:
                    if j - i + 1 > len(ans):
                        ans = s[i:j+1]
        return ans



s = Solution()
a = "bbb"
print(s.longestPalindrome(a))