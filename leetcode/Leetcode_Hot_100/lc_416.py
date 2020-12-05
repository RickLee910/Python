from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        temp = sum(nums)
        if temp % 2 == 1:
            return False
        else:
            temp //=2

        nums.sort()
        if nums[-1] > temp:
            return False
        if nums[-1] == temp :
            return True
        dp = [False] * (temp + 1)
        dp[0] = True
        for j in range(len(nums)):
            for i in range(temp,-1,-1):
                if i == nums[j]:
                    dp[i] = True
                    break
                dp[i] = dp[i] | dp[i - nums[j]]
            if dp[-1] == True:
                return True
        return False




s = Solution()
a = [2,2,3,5]
print(s.canPartition(a))