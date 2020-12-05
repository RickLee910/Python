class Solution:
    def subarraySum(self, nums, k: int) -> int:
        dic = {}
        count = 0
        pre = 0
        dic[0] = 1

        for i in range(len(nums)):
            pre += nums[i]

            if pre - k in dic.keys():
                count += dic[pre - k]
            if pre in dic:
                dic[pre] += 1
            else:
                dic[pre] = 1
        return count

s = Solution()
a = [1,1,-1,1]
print(s.subarraySum(a,0))