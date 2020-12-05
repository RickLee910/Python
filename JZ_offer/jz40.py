'''
数组中只出现一次的数（还有两次和三次）
做法：利用异或进行分组，保持两个组的数不同，相同的数在一个组内覆盖掉

'''


class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        xor1 = 0
        for i in range(len(array)):
            xor1 = xor1 ^ array[i]
        index = 1
        while ((index & xor1) == 0):
            index = index << 1
        a, b = 0, 0
        for i in range(len(array)):
            if index & array[i] == 0:
                a = a ^ array[i]
            else:
                b = b ^ array[i]
        return [a, b]


s = Solution()
a = [1, 3, 2, 3, 1, 4]
print(s.FindNumsAppearOnce(a))
