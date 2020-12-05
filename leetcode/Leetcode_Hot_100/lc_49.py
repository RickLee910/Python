from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        temp1 = {}
        for i in strs:
            temp = ''.join(sorted(i))
            if temp in temp1.keys():
                temp1[temp].append(i)
            else:
                temp1[temp] = [i]
        for i in temp1.values():
            ans.append(i)
        return ans
s = Solution()
a =  ["eat", "tea", "tan", "ate", "nat", "bat"]
print(s.groupAnagrams(a))
