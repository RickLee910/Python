from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        SUM = sum(nums)

        if (S+SUM) % 2 ==1 or SUM < S:
            return 0

        temp = (S+SUM) //2
        dp = [0] * (temp + 1)
        dp[0] = 1
        for n in nums:
            for i in range(temp,n-1,-1):
                dp[i] += dp[i-n]
        return dp[temp]
s = Solution()
a = [1,2,7,9,981]
S = 1000000000
print(s.findTargetSumWays(a,S))