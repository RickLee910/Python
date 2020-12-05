from typing import List
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if matrix == []:
            return 0
        row,col = len(matrix),len(matrix[0])
        dp = [[0]*col for i in range(row)]
        ans = 0
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == '0':
                    dp[i][j] = 0
                else:
                    if i - 1 < 0 or j - 1 < 0:
                        dp[i][j] = int(matrix[i][j])
                    elif dp[i - 1][j - 1] > 0 and dp[i - 1][j] > 0 and dp[i][j - 1] > 0:
                        dp[i][j] = (int(min([dp[i - 1][j - 1],dp[i - 1][j],dp[i][j - 1]]) ** 0.5) + 1) ** 2
                    else:
                        dp[i][j] = int(matrix[i][j])
                    ans = max(ans, dp[i][j])
        return ans
s = Solution()
a =  [["1","1","1","1","0"],["1","1","1","1","0"],["1","1","1","1","1"],["1","1","1","1","1"],["0","0","1","1","1"]]

print(s.maximalSquare(a))