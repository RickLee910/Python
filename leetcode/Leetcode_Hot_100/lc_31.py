class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        changed = False
        min_cur = nums[-1]
        min_index = -1
        temp = 0
        for i in range(len(nums) - 1, 0, -1):

            if nums[i] > nums[i - 1]:
                if min_cur <= nums[i - 1]:
                    min_cur = nums[i]
                    min_index = i
                for j in range(i,len(nums)):
                    if nums[j] > nums[i - 1]:
                        if min_cur > nums[j]:
                            min_cur = nums[j]
                            min_index = j
                changed = True
                nums[i - 1], nums[min_index] = nums[min_index], nums[i - 1]
                nums[i:] = sorted(nums[i:])
                break
        if not changed:
            for i in range(len(nums) // 2):
                nums[i], nums[-i - 1] = nums[-i - 1], nums[i]


s = Solution()
a = [1,5,1]
s.nextPermutation(a)
print(a)