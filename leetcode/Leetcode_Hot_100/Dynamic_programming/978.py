class Solution:
    def maxTurbulenceSize(self, arr) -> int:
        if len(arr) == 1:
            return 1
        dp = [0] * len(arr)
        # 0 >;1 <
        temp = -1
        if arr[0] != arr[1]:
            if arr[0] > arr[1]:
                temp = 0
            else:
                temp = 1
            dp[0] = 1
            dp[1] = 2

        else:
            dp[0], dp[1] = 1, 1
        maxd = dp[1]
        for i in range(2, len(arr)):
            if temp == 0:
                if arr[i - 1] < arr[i]:
                    dp[i] = dp[i - 1] + 1
                    temp = 1
                elif arr[i - 1] > arr[i]:
                    dp[i] = 2
                else:
                    temp = -1
                    dp[i] = 1
            elif temp == 1:
                if arr[i - 1] > arr[i]:
                    dp[i] = dp[i - 1] + 1
                    temp = 0
                elif arr[i - 1] < arr[i]:
                    dp[i] = 2
                else:
                    temp = -1
                    dp[i] = 1
            else:
                if arr[i - 1] != arr[i]:
                    dp[i] = dp[i - 1] + 1
                    if arr[i - 1] > arr[i]:
                        temp = 0
                    else:
                        temp = 1
                else:
                    dp[i] = 1
            maxd = max(maxd, dp[i])
        return maxd
s = Solution()
a = [2,0,2,4,2,5,0,1,2,3]
print(s.maxTurbulenceSize(a))