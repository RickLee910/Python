class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0,p2 = 0,len(nums)-1
        for i in range(len(nums)):

            while nums[i] == 2:
                if i > p2:
                    break
                nums[p2],nums[i] = nums[i],nums[p2]
                p2 -= 1
            while nums[i] == 0:
                nums[p0], nums[i] = nums[i], nums[p0]
                p0 += 1
                if p0 > i:
                    break
        return nums
s = Solution()
a = [2,0,2,1,1,0]
s.sortColors(a)
print(a)