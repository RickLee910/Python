class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        visited = {}
        res = 0
        for i in range(1,n+1):
            temp = i
            count = 0
            while i:
                if i in visited:
                    count += visited[i]
                    break
                if i % 10 == 1:
                    count += 1
                i //= 10
            visited[temp] = count
            if count > 0:
                res += 1
        return res
        # digit, res = 1, 0
        # high, cur, low = n // 10, n % 10, 0
        # while high != 0 or cur != 0:
        #     if cur == 0: res += high * digit
        #     elif cur == 1: res += high * digit + low + 1
        #     else: res += (high + 1) * digit
        #     low += cur * digit
        #     cur = high % 10
        #     high //= 10
        #     digit *= 10
        # return res
s = Solution()
a = 55
print(s.NumberOf1Between1AndN_Solution(a))