class Solution:
    def trap(self, height) -> int:
        if height == []:
            return 0
        res = []
        max_h = max(height)
        maxh_index = height.index(max_h)

        def countleft(h,i):
            if h == []:
                return
            cur_max_h = max(h)
            cur_maxh_index = height.index(cur_max_h)
            res.append(cur_max_h * (i - cur_maxh_index - 1) - sum(height[cur_maxh_index + 1:i]))
            countleft(height[:cur_maxh_index], cur_maxh_index)

        def countright(h, i):
            if h == []:
                return
            cur_max_h = max(h)
            cur_maxh_index = h.index(cur_max_h)
            res.append(cur_max_h * cur_maxh_index - sum(height[i+1:i+cur_maxh_index + 1]))
            countright(height[i+cur_maxh_index + 2:], i+cur_maxh_index+1)

        countright(height[maxh_index+1:],maxh_index)
        countleft(height[:maxh_index], maxh_index)

        return sum(res)





s = Solution()
a = []
print(s.trap(a))