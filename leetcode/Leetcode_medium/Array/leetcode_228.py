class Solution:
    def summaryRanges(self, nums):
        left,right = 0, 0
        nums += [-1]
        temp = []
        for i in range(len(nums) - 1):
            if nums[i + 1] == nums[i] + 1:
                right = i + 1
            else:
                if right > left:
                    s = str(nums[left]) + "->" + str(nums[right])
                    temp.append(s)
                    left = right + 1
                else:
                    temp.append(str(nums[left]))
                    left += 1
        return temp

s =Solution()
a = []
print(s.summaryRanges(a))