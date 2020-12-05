class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i,len(matrix[0])):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

        for i in range(len(matrix)):
            matrix[i].reverse()



s = Solution()
a = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
s.rotate(a)
print(a)