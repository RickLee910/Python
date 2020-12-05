'''
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，例如，如果输入如下4 X 4矩阵：
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.

做法：设置左右上下界限，四次循环计算
TIPS：注意及时break
'''

class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        if len(matrix) == 1:
            return matrix[0]
        res = []
        if len(matrix[0]) == 1:
            for i in range(len(matrix)):
                res.append(matrix[i][0])
            return res
        len_row_R, len_col_R = len(matrix),len(matrix[0])
        len_row_L, len_col_L = 0, 0
        i,j = 0,0

        while len_row_L < len_row_R and len_col_L < len_col_R:
            for j in range(len_col_L,len_col_R):
                res.append(matrix[i][j])
            if len_row_L+1 >= len_row_R:
                break
            for i in range(len_row_L+1,len_row_R):
                res.append(matrix[i][j])

            for j in range(len_col_R-2,len_col_L -1,-1):
                res.append(matrix[i][j])
            for i in range(len_row_R-2,len_row_L,-1):
                res.append(matrix[i][j])
            len_row_L += 1
            len_col_L += 1
            len_row_R -= 1
            len_col_R -= 1
        return res
s = Solution()
a = [[1,2,3],[6,7,8],[11,12,13]]
print(s.printMatrix(a))