'''
最小K个数

输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4。

做法：考察大根堆 maxHeap,adjustDown
'''


class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        arr = [0] * (k + 1)

        def adjustDown(arr, k, length):
            arr[0] = arr[k]
            i = 2 * k
            while i < length:
                if i + 1 < length and arr[i + 1] > arr[i]:
                    i += 1
                if i + 1 > length or arr[0] >= arr[i]:
                    break
                else:
                    arr[k] = arr[i]
                    k = i
                i *= 2
            arr[k] = arr[0]

        def buildmaxHeap(arr, length):
            for i in range((length - 1) // 2, 0, -1):
                adjustDown(arr, i, len(arr))

        if k > len(tinput) or k == 0:
            return []
        for i in range(1, k + 1):
            arr[i] = tinput[i - 1]
        buildmaxHeap(arr, k + 1)
        for i in range(k, len(tinput)):
            if tinput[i] < arr[1]:
                arr[1] = tinput[i]
                adjustDown(arr, 1, k + 1)
        return list(set(arr[1:]))

s = Solution()
a = [1,3,5,7,2,4,6,8]
print(s.GetLeastNumbers_Solution(a,4))