'''
数字在升序数组中出现的次数

做法：二分查找
TIPS：注意开始时把最后一位加上，防止计算时丢失最后一位的值
'''
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        def binasearch(data, l, r):
            if l >= r:
                return 0
            mid = int(l + (r - l) // 2)

            if data[mid] == k:

                return 1 + binasearch(data, l, mid) + binasearch(data, mid + 1, r )
            elif data[mid] > k:
                return binasearch(data, l, mid)
            else:
                return binasearch(data, mid + 1, r)

        return binasearch(data, 0, len(data))
s = Solution()
a = [1,2,3,3,3,3]
print(s.GetNumberOfK(a,3))