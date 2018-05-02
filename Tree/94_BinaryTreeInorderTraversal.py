class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
#94 Binary Tree Inorder Traversal Recursive 29.92%
class Solution_R(object):
    def inorderTraversal(self, root):
        res = []
        if root == None:
            return []
        self.helper(root,res)
        return res
    
    def helper(self, root, res):
        if root.left != None:
            self.helper(root.left,res)
        res.append(root.val)
        if root.right != None:
            self.helper(root.right,res)

#94 Binary Tree Inorder Traversal Iteration Stack 21%
class Solution_S(object):
    def inorderTraversal(self, root):
        if root == None:
            return []
        
        res = []
        stack = []

        while root or len(stack) != 0:
            while root:
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            res.append(root.val)
            root = root.right
        
        return res


#94. BinaryTreeInorderTraversal Morris Traversal

class Solution(object):
    def inorderTraversal(self,root):
        if root == None:
            return []
        res = []
        cur = root
        while cur != None:
            if cur.left == None:
                res.append(cur.val)
                cur = cur.right
            else:
                prev = cur.left
                while prev.right != None:
                    prev = prev.right
                prev.right = cur
                temp = cur
                cur = cur.left
                temp.left = None
        return res
            


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6

my_s = Solution()
result = my_s.inorderTraversal(node1)
print(result)