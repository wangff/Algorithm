# Solution_1 Recursive Approach 99s
import sys
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution_1(object):
    def isValidBST(self,root):
        prev = [-sys.maxsize]
        ret = self.helper(root,prev)
        return ret
    
    def helper(self,root,prev):
        if not root: return True
        if not self.helper(root.left,prev): return False
        if prev[-1] >= root.val: return False
        prev[-1] = root.val
        if not self.helper(root.right,prev): return False
        return True

import sys 
#Solution2 Iterating with stack 99s
class Solution_2(object):
    def isValidBST(self,root):
        prev = -sys.maxsize
        curr = root
        stack = []
        while curr or len(stack)!=0:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            if curr.val <= prev:
                return False
            else:
                prev = curr.val
            
            curr = curr.right
        return True

# Solution 3 Morris Traversal 64
import sys
class Solution(object):
    def isValidBST(self, root):
        prev = -sys.maxsize
        curr = root
        while curr:
            if not curr.left:
                if prev >= curr.val:
                    return False
                else:
                    prev = curr.val
                curr = curr.right
            else:
                preNode = curr.left
                while preNode.right:
                    preNode = preNode.right
                preNode.right = curr
                temp = curr
                curr = curr.left
                temp.left = None
        return True

t5 = TreeNode(5)
t1 = TreeNode(1)
t4 = TreeNode(7)
t3 = TreeNode(3)
t6 = TreeNode(6)

t5.left = t1
t5.right = t4
# t4.left = t3
# t4.right = t6

obj = Solution()
res = obj.isValidBST(t5)
print(res)