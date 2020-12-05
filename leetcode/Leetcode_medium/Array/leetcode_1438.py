from collections import deque
class Solution:
    def longestSubarray(self, nums, limit: int) -> int:
        maxq, minq = deque(), deque()
        i = 0
        for n in nums:
            while maxq and n > maxq[-1]: maxq.pop()
            while minq and n < minq[-1]: minq.pop()
            maxq.append(n)
            minq.append(n)
            if maxq[0] - minq[0] > limit:
                if maxq[0] == nums[i]: maxq.popleft()
                if minq[0] == nums[i]: minq.popleft()
                i += 1
        return len(nums) - i




    def longestSubarray1(self, nums, limit: int) -> int:
        count = 1
        max_count = 1
        left = 0
        j = 1
        if len(nums) == 1:
            return count
        for i in range(1,len(nums)):
            temp = nums[left:j+1]
            temp.sort()
            while temp[-1] - temp[0] <= limit:
                count += 1
                j+= 1
                temp = nums[left:j + 1]
                temp.sort()
                if j >= len(nums):
                    break
            max_count = max(max_count, count)
            count -= 1
            left = i
        return max_count
s = Solution()
a = [1,5,6,7,8,10,5,6,5]
print(s.longestSubarray(a,4))