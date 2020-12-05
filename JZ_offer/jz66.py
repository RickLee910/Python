# -*- coding: utf-8 -*-
# __author__:song
# 2020/12/4 15:37
'''
矩阵中的路径
做法：dfs回溯
'''
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        if path == '':
            return True
        def findpath(i,j,k):
            if i == rows or i < 0 or j == cols or j < 0 or mat[i][j] != path[k]:
                return False
            if k == len(path) - 1:
                return True
            temp = mat[i][j]
            mat[i][j] = ''
            res = findpath(i+1,j,k+1) or findpath(i-1,j,k+1) or findpath(i,j+1,k+1) or findpath(i,j-1,k+1)
            mat[i][j] = temp
            return res

        mat = [[0] * cols for _ in range(rows)]
        k = 0
        for i in range(rows):
            for j in range(cols):
                mat[i][j] = matrix[k]
                k+=1
        for i in range(rows):
            for j in range(cols):
                if findpath(i,j,0):
                    return True
        return False
s = Solution()
a = "ABCESFCSADEE"
b = "ABCCED"
print(s.hasPath(a,3,4,b))

