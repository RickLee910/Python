class Solution:
    def canJump(self, nums) -> bool:
        l = len(nums)
        def dfs(i):
            if i ==l-1:
                return True
            if nums[i] == 0:
                return
            for j in range(nums[i]):
                if i + nums[i] - j < l:
                    if dfs(i + nums[i] - j):
                        return True
        return dfs(0) == True
s = Solution()
a = [2,3,1,1,4]
print(s.canJump(a))