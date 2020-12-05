class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        length = 0
        max_length = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if stack == []:
                    stack.append(i)
                else:
                    length = i-stack[-1]
                    max_length = max(max_length,length)
        return max_length
    '''
    #动态规划
    def longestValidParentheses(self, s: str) -> int:
        l =  len(s)
        dp = [0] * l
        if l == 0:
            return 0
        for i in range(l):
            if s[i] ==')':
                if i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                    dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2
        return max(dp)'''
s = Solution()
a = "()((())))))("
print(s.longestValidParentheses(a))