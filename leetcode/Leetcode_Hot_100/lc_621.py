from collections import Counter
class Solution:
    def leastInterval(self, tasks, n: int) -> int:
        if n == 0:
            return len(tasks)
        dic = Counter(tasks)

        temp = sorted(dic.items(), key=lambda x: x[1], reverse=True) #从大到小排序

        L = len(tasks)

        extra = 0
        step = temp[0][1]
        for i in temp:
            if i[1]== step:
                extra += 1
            else:
                break
        return extra + max((n+1)*(step-1),L - extra)



s = Solution()
a = ["A","A","A","A","A","A","B","C","D","E","F","G"]
print(s.leastInterval(a,2))