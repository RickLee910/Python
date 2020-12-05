from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        dp = [1]* len(nums)
        ans = 1
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])
            ans = max(ans,dp[i])
        return ans
s = Solution()
a =  [1,3,6,7,9,4,10,5,6]
print(s.lengthOfLIS(a))