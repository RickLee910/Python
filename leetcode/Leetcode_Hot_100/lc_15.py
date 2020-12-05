class Solution:
    def threeSum(self, nums):
        ans = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                ans = list(set(tuple(i) for i in ans))
                ans = [list(i) for i in ans]
                return ans
            if i > 0 and nums[i] == nums[i-1]:
                continue
            L = i+1
            R = len(nums)- 1
            while L < R:
                temp = nums[i] + nums[L] + nums[R]
                if temp == 0:
                    ans.append([nums[i],nums[L],nums[R]])
                    L += 1
                    R -= 1
                elif temp > 0:
                    R -= 1
                else:
                    L += 1
        ans = list(set(tuple(i) for i in ans))
        ans = [list(i) for i in ans]
        return ans
s = Solution()
a =[-2,0,0,2,2]
print(s.threeSum(a))