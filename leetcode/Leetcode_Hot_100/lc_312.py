from typing import List
class Solution:
    #回溯法 超时

    # def maxCoins(self, nums: List[int]) -> int:
    #     self.ans = 0
    #     def helper(nums, coin):
    #         if len(nums) == 0:
    #             self.ans = max(self.ans, coin)
    #             return
    #         for i in range(len(nums)):
    #             temp = nums[i]
    #             delta = nums[i] * (nums[i - 1] if i - 1 >= 0 else 1) * (nums[i + 1] if i + 1 <= len(nums) - 1 else 1)
    #             nums.pop(i)
    #             helper(nums, coin + delta)
    #             nums.insert(i, temp)
    #
    #
    #     helper(nums, 0)
    #     return self.ans
    #动态规划
    # def maxCoins(self, nums: List[int]) -> int:
    #     def helper(nums,i,j):
    #         if i > j:
    #             return 0
    #         if dp[i][j] > 0:
    #             return dp[i][j]
    #         for k in range(i,j+1):
    #             left = helper(nums,i,k-1)
    #             right = helper(nums,k+1,j)
    #             delta = nums[k] * nums[i-1] * nums[j+1]
    #             dp[i][j] = max(dp[i][j],left+right+delta)
    #         return dp[i][j]
    #
    #     l = len(nums)
    #     nums.append(1)
    #     nums.insert(0,1)
    #     dp = [[0]*(l+2) for _ in range(l+2)]
    #     ans = helper(nums,1,l)
    #     return ans
    #动态规划优化
    def maxCoins(self, nums: List[int]) -> int:
        l = len(nums)
        nums.insert(0,1)
        nums.append(1)
        dp = [[0]*(l+2) for _ in range(l+2)]
        for lengt in range(1,l+1):
            for i in range(1,l-lengt+2):
                j = i + lengt - 1
                for k in range(i,j+1):

                        dp[i][j] = max(dp[i][k - 1] + dp[k + 1][j] + nums[k] * nums[i - 1] * nums[j + 1],dp[i][j])
        return dp[1][l]

s =Solution()
a= [3,1,5,8]
print(s.maxCoins(a))