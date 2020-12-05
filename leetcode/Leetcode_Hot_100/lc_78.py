class Solution:
    def subsets(self, nums):
        res = [[]]
        num = nums.copy()
        while nums:

            temp = [nums.pop(0)]
            if isinstance(temp[0],list):
                res.append(temp[0])
                for i in num[num.index(temp[0][-1])+1:]:
                    nums.append(temp[0] + [i])
            else:
                res.append(temp)
                for i in num[num.index(temp[-1])+1:]:
                    nums.append(temp + [i])

        return res
s = Solution()
a = [1,2,3,4]
print(s.subsets(a))