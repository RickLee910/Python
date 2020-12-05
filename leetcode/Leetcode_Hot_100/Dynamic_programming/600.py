class Solution:
    def findIntegers(self, num: int) -> int:
        def fib(n):
            if n == 0 or n == 1:
                return n+1
            a = 1
            b = 2
            n = n - 2
            while n >= 0:
                a,b = b, a+b
                n -= 1
            return b
        if num == 0 or num == 1:
            return num + 1
        nbit = 0
        while num >> nbit:
            nbit += 1
        #判断头两位
        #为11时
        if (num >> (nbit - 2)) == 3:
            return fib(nbit)
        else:
            mask = (1 << (nbit-1)) - 1
            return fib(nbit-1) + self.findIntegers(num & mask)
s = Solution()
a = 5
print(s.findIntegers(a))