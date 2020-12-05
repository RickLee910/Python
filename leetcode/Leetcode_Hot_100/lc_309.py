from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = len(prices)
        if l < 2:
            return 0
        buy = [0] * l
        sell = [0] * l
        cool = [0] * l
        buy[0] = -prices[0]
        for i in range(1,l):
            sell[i] = max(buy[i-1]+prices[i],sell[i-1])
            buy[i] = max(cool[i-1]-prices[i],buy[i-1])
            cool[i] = max(sell[i-1], cool[i-1])
        return max(sell[-1],buy[-1],cool[-1])
s = Solution()
a = [1,2,3,0,2]
print(s.maxProfit(a))