class Solution:
    def exist(self, board, word: str) -> bool:
        m = len(board)
        n = len(board[0])

        def dfs(i,j,str):
            if str == '':
                return True
            if i+1 < m and step[i+1][j] == False and board[i+1][j] == str[0]:
                step[i+1][j] = True
                if dfs(i+1,j,str[1:]):
                    return True
            if i-1 >=0 and step[i-1][j] == False and board[i-1][j] ==str[0]:
                step[i - 1][j] = True
                if dfs(i-1,j,str[1:]):return  True
            if j+1 < n and step[i][j+1] == False and board[i][j+1] ==str[0]:
                step[i][j + 1] = True
                if dfs(i,j+1,str[1:]): return True
            if j-1 >= 0 and step[i][j-1] == False and board[i][j-1] == str[0]:
                step[i][j - 1] = True
                if dfs(i,j-1,str[1:]):return True
            step[i][j] = False
        for x in range(m):
            for y in range(n):
                if board[x][y] == word[0]:
                    step = [[False] * n for i in range(m)]
                    step[x][y] = True
                    if dfs(x,y,word[1:]):
                        return True
        return False
s = Solution()
a = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
print(s.exist(a,"ABCB"))