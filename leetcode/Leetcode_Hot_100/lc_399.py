from typing import List
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # 构造图，equations的第一项除以第二项等于value里的对应值，第二项除以第一项等于其倒数
        graph = {}
        for (x,y),v in zip(equations,values):
            if x in graph:
                graph[x][y] = v
            else:
                graph[x] = {y:v}
            if y in graph:
                graph[y][x] = 1 / v
            else:
                graph[y] = {x:1/v}

        def dfs(x,y):
            if x not in graph:
                return float(-1)
            if x == y:
                return float(1)
            for node in graph[x].keys():
                if node == y:
                    return graph[x][y]
                elif node not in visited:
                    visited.add(node)
                    v = dfs(node,y)
                    if v != -1:
                        return v*graph[x][node]
            return -1
        res = []
        for i in queries:
            visited = set()
            res.append(dfs(i[0],i[1]))
        return res
s = Solution()
a = [["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]]
v = [3.0,4.0,5.0,6.0]
q = [["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]]
print(s.calcEquation(a,v,q))