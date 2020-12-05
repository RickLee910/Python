class Solution:
    def maxProduct(self, nums) -> int:
        Max, Min = [0] * len(nums), [0] * len(nums)
        Max[0],Min[0] = nums[0],nums[0]
        for i in range(1, len(nums)):
            Max[i] = max(Max[i-1] * nums[i], max(Min[i - 1] * nums[i], nums[i]))
            Min[i] = min(Min[i-1] * nums[i], min(Max[i - 1] * nums[i], nums[i]))
        return max(Max)
s = Solution()
a = [-2,-3,7]
print(s.maxProduct(a))