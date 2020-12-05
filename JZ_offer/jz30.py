'''
连续子苏红组最大和

做法：在原list上动态规划，判断上一是否是负数，如果不是累加，是则维护自己本身的值，循环

'''

class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        max_num = array[0]
        for i in range(1,len(array)):
            array[i] += array[i-1] if array[i-1] >0 else 0
            max_num = max(max_num,array[i])
        return max_num

s = Solution()
a = [-2,-8,-1,-5,-9]
print(s.FindGreatestSumOfSubArray(a))