class Solution:
    def merge(self, intervals):
        if len(intervals) <= 1:
            return intervals
        intervals.sort()
        ans = []
        for i in range(1,len(intervals)):
            if intervals[i][0] > intervals[i-1][1]:
                ans.append(intervals[i-1])
            else:
                temp = []
                temp.append(min(intervals[i-1][0],intervals[i][0]))
                temp.append(max(intervals[i-1][1],intervals[i][1]))
                intervals[i] = temp.copy()

        ans.append(intervals[-1])
        return ans
s = Solution()
a = [[1,4],[0,0]]
print(s.merge(a))