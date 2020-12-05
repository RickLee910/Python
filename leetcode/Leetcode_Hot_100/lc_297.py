# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from collections import deque
class Codec:
    def serialize(self, root):
        if not root:
            return
        l=[root]
        l_copy=[]
        a,ans=[],[root.val]
        while True:
            for i in l:
                if i.left:
                    l_copy.append(i.left)
                    a.append(i.left.val)
                else:
                    a.append(None)
                if i.right:
                    l_copy.append(i.right)
                    a.append(i.right.val)
                else:
                    a.append(None)
            if a==[]:
                break
            l=l_copy.copy()
            ans+=a
            l_copy,a=[],[]
        while ans[-1]!=0 and not ans[-1]:
            ans.pop()
        return self.deserialize(ans)

    def deserialize(self,data):
        print(data)
        return data




# Your Codec object will be instantiated and called as such:
a = "[1,2,3,null,null,4,5,6,7]"
ser = Codec()
deser = Codec()
ans = deser.deserialize(ser.serialize(a))
print(ans)