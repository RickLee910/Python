from collections import deque
class Solution:
    def findLengthOfShortestSubarray(self, arr) -> int:
        if len(arr) == 1:
            return 0
        count = 0
        s = len(arr)
        l, r = 0, s - 1
        lr, rl = 0, s - 1
        i, j = 0, s - 1
        temp1, temp2 = [], []
        while i < s - 1:
            if arr[i] <= arr[i + 1]:
                lr += 1
                i += 1
            else:

                break
        temp1 = arr[l:lr + 1]
        if len(temp1) == s:
            return 0
        while j > 0:
            if arr[j - 1] <= arr[j]:
                rl -= 1
                j -= 1
            else:

                break
        temp2 = arr[rl:r + 1]
        count = s - len(temp1) -len(temp2)
        while temp1 != [] and temp2 != []:
            if temp1[0] > temp2[0]:
                temp1.pop(0)
                temp2.pop(0)
                count += 1
            else:
                temp1.pop(0)

        return count
s = Solution()
a = [1,2,3,10,4,2,3,5]
print(s.findLengthOfShortestSubarray(a))



