class Solution:
    def getWinner(self, arr, k: int) -> int:
        if k >= len(arr):
            return max(arr)
        count = 0
        if k == 1:
            return max(arr[0], arr[1])
        while count != k:
            if arr[0] > arr[1]:
                count += 1
                if count == k:
                    return arr[0]
                arr.append(arr[1])
                del arr[1]
            else:
                count = 1
                arr.append(arr[0])
                del arr[0]
s = Solution()
a = [1,25,35,42,68,70]
print(s.getWinner(a, 1))