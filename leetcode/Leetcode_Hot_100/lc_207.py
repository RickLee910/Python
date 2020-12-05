from typing import List
from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dic = {}
        indeg = [0]*numCourses
        for i,j in prerequisites:
            if j in dic.keys():
                dic[j].append(i)
            else:
                dic[j] = [i]
            indeg[i] += 1
        res = 0
        q = deque()
        for i in range(numCourses):
            if indeg[i] == 0:
                q.append(i)
        while q:
            i = q.popleft()
            res += 1
            if i in dic.keys():
                for j in dic[i]:
                    indeg[j] -= 1
                    if indeg[j] == 0:
                        q.append(j)
        return res >= numCourses

s = Solution()
a = 2
b = [[1,0],[0,1]]
print(s.canFinish(a,b))
