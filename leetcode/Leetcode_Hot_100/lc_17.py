from collections import deque
class Solution:
    def letterCombinations(self, digits: str):
        p = {'2':'abc',
                '3':'def',
                '4':'ghi',
                '5':'jkl',
                '6':'mno',
                '7':'pqrs',
                '8':'tuv',
                '9':'wxyz'}
        if len(digits) == 1:
            return list(p[digits[0]])
        if digits == '':
            return []
        d = deque()
        for i in range(len(p[digits[0]])):
            d.append(p[digits[0]][i])

        j = 1
        while j < len(digits):
            for i in range(len(d)):
                temp = d.popleft()
                for k in p[digits[j]]:
                    temp1 = temp + k
                    d.append(temp1)
            j += 1
        return list(d)
s = Solution()
a = '23456'
print(s.letterCombinations(a))

