class Solution:
    def combinationSum(self, candidates, target: int):
        candidates.sort()
        n = len(candidates)
        res = []
        def helper(start, S, temp):
            if start == n or S > target:
                return
            if S == target:
                res.append(temp)
                return
            helper(start, S + candidates[start],temp + [candidates[start]])
            helper(start + 1, S,temp)
        helper(0,0,[])
        return res
s = Solution()
a = [2,3,5]
print(s.combinationSum(a,8))



