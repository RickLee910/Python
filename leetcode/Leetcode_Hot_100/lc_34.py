class Solution:
    def searchRange(self, nums, target: int):
        low,high = 0, len(nums) -1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                low = high = mid
                low_empty, high_empty = False,False
                for i in range(1,len(nums)):
                    if mid - i >=0 and not low_empty:
                        if nums[mid - i] == target:
                            low = mid - i
                        else:
                            low_empty = True
                    if mid + i <len(nums) and not high_empty:
                        if nums[mid + i] == target:
                            high = mid + i
                        else:
                            high_empty = True
                return [low, high]
            elif nums[mid] < target:
                low = mid + 1
            else:high = mid-1
        return [-1,-1]
s = Solution()
a = [5,7,7,8,8,10]
print(s.searchRange(a,8))