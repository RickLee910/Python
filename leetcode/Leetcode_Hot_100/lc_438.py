from typing import List
from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        h = Counter(p)
        i = 0
        res = []
        for i in range(len(s) - len(p)+1):
            temp = Counter(s[i:i+len(p)])
            if temp == h:
                res.append(i)

        # while i < len(s) -len(p)+1:
        #
        #     # temp = h.copy()
        #     # if s[i] in temp.keys():
        #     #     pre = i
        #     #     while s[i] in temp.keys():
        #     #         temp[s[i]] -= 1
        #     #         if temp[s[i]] < 0:
        #     #             break
        #     #         i += 1
        #     #         if sum(temp.values()) == 0:
        #     #             res.append(pre)
        #     #             break
        #     #     i = pre + 1
        #     # else:
        #     #     i += 1

        return res
s = Solution()
a = "abacbabc"
b= 'abc'
print(s.findAnagrams(a,b))
