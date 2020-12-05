# -*- coding: utf-8 -*-
# __author__:song
# 2020/12/4 16:42
'''
机器人的运动范围
做法：递归或遍历
'''
class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here

        vis = set()
        def helper(i,j,si,sj):
            if not i < rows or not j < cols or si + sj > threshold or (i,j) in vis:
                return 0
            vis.add((i,j))
            return 1 + helper(i+1,j,si+1 if (i + 1)%10 else si - 8,sj) +  helper(i,j+1,si,sj+1 if (j + 1)%10 else sj - 8)

        return helper(0, 0,0,0)
s = Solution()
print(s.movingCount(5,10,10))