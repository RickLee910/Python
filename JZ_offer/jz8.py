'''
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。

做法：同斐波那契一样，利用 递归，动态规划dp[n] = dp[n-1] + dp[n-2](动态规划可以正向你想思考)
'''
class Solution:
    def jumpFloor(self, number):
        # write code here
        if number < 2:
            return number
        dp = [0] * (number + 1)
        dp[0], dp[1] = 1, 1
        for i in range(2, number + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[number]
