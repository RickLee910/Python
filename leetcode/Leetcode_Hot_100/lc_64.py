from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0] * n]*m

        for i in range(0,m):
            for j in range(0,n):
                if i - 1 >= 0 and j - 1 >= 0:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
                elif i == 0 and j != 0:
                    dp[i][j] = dp[i][j - 1] + grid[i][j]
                elif j == 0 and i != 0:
                    dp[i][j] = dp[i - 1][j] + grid[i][j]
                else:
                    dp[i][j] = grid[i][j]
        return dp[-1][-1]
s = Solution()
a = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
print(s.minPathSum(a))