from TreeNode import TreeNode
#solution one using recursive
class Solution_Recur(object):
    def invertTree(self,root):
        if root == None:
            return
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

#solution two using interative method
class Solution(object):
    def invertTree(self,root):
        stack =  []
        stack.append(root)
        while len(stack)!=0:
            t = stack.pop()
            if t == None: continue
            t.left, t.right = t.right, t.left
            stack.append(t.left)
            stack.append(t.right)
        
        return root

