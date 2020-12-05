from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 自底向上
        # dp[i] 表示金额为i需要最少的硬币
        # dp[i] = min(dp[i], dp[i - coins[j]]) j所有硬币

        # dp = [float("inf")] * (amount + 1)
        # dp[0] = 0
        # for i in range(1, amount + 1):
        #     dp[i] = min(dp[i - c] if i - c >= 0 else float("inf") for c in coins) + 1
        # return dp[-1] if dp[-1] != float("inf") else -1
        #自顶向下
        # import functools
        # @functools.lru_cache(None)
        # def helper(amount):
        #     if amount == 0:
        #         return 0
        #
        #
        #     return min(helper(amount - i) if amount - i >= 0 else float('inf') for i in coins) + 1
        #
        #
        # res = helper(amount)
        # return res if res != float('inf') else -1
        #BFS
        # if amount == 0:
        #     return 0
        # s = [amount]
        # visited = set()
        # res = 0
        # while s:
        #     for i in range(len(s)):
        #         temp = s.pop(0)
        #         for j in coins:
        #             if temp - j > 0 and (temp - j) not in visited:
        #                 s.append(temp - j)
        #                 visited.add(temp - j)
        #             elif temp - j == 0:
        #                 return res + 1
        #     res += 1
        # return -1
        #DFS
        self.res = 100000
        coins.sort()
        coins = coins[::-1]
        def dfs(k,amount,depth):
            if amount == 0:
                self.res = min(self.res, depth)
                return
            for i in range(k,len(coins)):
                if (self.res - depth) * coins[i] < amount:
                    break
                if amount - coins[i] >= 0:
                    dfs(i,amount - coins[i],depth+1)

        for i in range(len(coins)):
            dfs(i, amount, 0)
        return self.res if self.res != 100000 else -1
s = Solution()
a = [1,2,5]
print(s.coinChange(a,11))