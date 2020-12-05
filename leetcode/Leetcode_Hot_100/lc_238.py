from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [nums[-1]]
        for i in range(len(nums)-2,-1,-1):
            ans.append(nums[i]*ans[len(nums) - i - 2])
        ans = ans[::-1]
        ans.pop(0)
        temp = nums[0]

        for i in range(1,len(ans)):
            ans[i] *= temp
            temp *= nums[i]
        ans.append(temp)
        return ans
s = Solution()
a = [1,2,3,4]
print(s.productExceptSelf(a))