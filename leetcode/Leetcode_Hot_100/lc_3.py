class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1 or len(s) == 0:
            return len(s)
        max_l, cur = 0, 1
        l,r = 0, 1
        temp = {}
        temp[s[l]] = l
        while r < len(s):
            if s[r] in temp.keys():
                max_l = max(max_l, cur)
                while s[l] != s[r]:
                    temp.pop(s[l])
                    cur -= 1
                    l += 1
                temp.pop(s[l])
                l+=1
                cur -= 1
            else:
                temp[s[r]] = r
                r += 1
                cur += 1
        return max(max_l, cur)

s = Solution()
a = "abcabcbb"
print(s.lengthOfLongestSubstring(a))
