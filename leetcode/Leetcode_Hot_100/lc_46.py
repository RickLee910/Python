class Solution:
    #bfs
    def permute(self, nums):

        ans = []
        l = len(nums)
        temp = []
        for i in nums:
            temp.append([i])
        while temp:
            for i in range(len(temp)):
                temp1 = temp.pop(0)
                if len(temp1) == l:
                    ans.append(temp1)
                    continue
                for j in range(len(nums)):
                    if nums[j] not in temp1:
                        temp.append(temp1 + [nums[j]])
        return ans



    #dfs
    '''
        def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, size, depth, path, used, res):
            if depth == size:
                res.append(path[:])
                return

            for i in range(size):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])

                    dfs(nums, size, depth + 1, path, used, res)

                    used[i] = False
                    path.pop()

        size = len(nums)
        if len(nums) == 0:
            return []

        used = [False for _ in range(size)]
        res = []
        dfs(nums, size, 0, [], used, res)
        return res
    '''


s = Solution()
a = [1,2,3]
print(s.permute(a))