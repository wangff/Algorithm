# 572 Subtree of another tree
# Preorder traversal

from TreeNode import TreeNode
# Solution 1 By comparison of nodes
class Solution_comp(object):
    def isSubtree(self,s,t):
        if not s: return False
        curr = self.isSameTree(s,t)
        left = self.isSubtree(s.left,t)
        right = self.isSubtree(s.right,t)
        return left or right or curr
        
     
    
    def isSameTree(self,s,t):
        if not s and not t: return True
        if not s or not t : return False
        curr = (s.val == t.val)
        left = self.isSameTree(s.left,t.left)
        right = self.isSameTree(s.right,t.right)
        return curr and left and right


# Soluton 2 Using preorder traverse

class Solution(object):
    def isSubtree(self,s,t):
        sStr = self.preorder(s,True)
        tStr = self.preorder(t,True)

        return tStr in sStr
    
    def preorder(self,node, isleft):
        if not node:
            return "lnull" if isleft else "rnull"
        curr = "#"+str(node.val)
        left = " "+self.preorder(node.left,True)
        right = " "+self.preorder(node.right, False)
        return curr + left + right

