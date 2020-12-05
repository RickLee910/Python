from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        temp = nums[:k]
        max_num = max(temp)
        ans = [max_num]
        for i in range(1,len(nums) - k + 1):
            if nums[i+k-1] >= nums[i-1]:
                max_num = max(nums[i+k-1],max_num)
            else:
                if max_num == nums[i-1]:
                    max_num = max(nums[i:i+k])
                else:
                    max_num = max(nums[i + k - 1], max_num)
            ans.append(max_num)
        return ans
s = Solution()
a = [1,3,-1,-3,5,3,6,7]
print(s.maxSlidingWindow(a,3))
