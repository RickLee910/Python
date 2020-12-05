class Solution:
    def countSubstrings(self, s: str) -> int:
        def count(left,right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                self.res += 1
                left -= 1
                right += 1
        self.res = 0
        for i in range(len(s)):
            count(i,i+1)
            count(i-1,i+1)
        return self.res + len(s)
s = Solution()
a = "baaccbdabdcaacbaacdcbdacdcccadadcababcaaddbccbcccadbcaddacdaddddabddaccccdddcacbdbddcaaabbcc"
print(s.countSubstrings(a))
