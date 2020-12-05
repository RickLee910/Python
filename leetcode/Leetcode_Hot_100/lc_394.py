class Solution:
    def decodeString(self, s: str) -> str:
        #辅助栈
        # stack = []
        #
        # for i in s:
        #     stack.append(i)
        #     if i == ']':
        #         j = ''
        #         while stack != []:
        #             j = stack.pop() + j
        #             if j[0] == '[':
        #                 break
        #         num = ''
        #         while stack != []:
        #             if stack[-1].isdigit():
        #                 num = stack.pop() + num
        #
        #             else:
        #                 break
        #         if num != '':
        #
        #             stack.append(int(num) * j[1:-1])
        #         else:
        #             stack.append(j[1:-1])
        # return ''.join(stack)
        #递归

        def build(s,i):
            res,num = '',''
            while i < len(s):
                if s[i].isdigit():
                    num += s[i]
                elif s[i] == '[':
                    i,temp = build(s,i+1)
                    res += int(num) * temp

                    num = ''
                elif s[i] == ']':
                    return i,res
                else:
                    res += s[i]
                i+= 1
            return res
        return build(s,0)


s = Solution()
a = "100[leetcode]"
print(s.decodeString(a))