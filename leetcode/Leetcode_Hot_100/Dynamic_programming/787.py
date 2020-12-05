from typing import List
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        dp = [[float('inf')] * (K+2) for _ in range(n)]
        for i in range(K+2):
            dp[src][i] = 0
        for i in range(1,K+2):
            for flight in flights:
                # 如果从src至多经过k - 1站可达flight[0]
                if dp[flight[0]][i] != 'inf':
                    # 更新从src至多经过k站到达flight[1]
                    dp[flight[1]][i] = min(dp[flight[1]][i],dp[flight[0]][i-1] + flight[2])
        if dp[dst][K+1] == float('inf'):
            return -1
        return dp[dst][K+1]
s = Solution()
a = [[0,1,100],[1,2,100],[0,2,500]]
print(s.findCheapestPrice(3,a,0,2,1))