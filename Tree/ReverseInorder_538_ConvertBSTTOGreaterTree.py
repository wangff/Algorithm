# 538. Convert BST to Greater Tree
# reverse in-order tree traversal

# Solution 1 recursive 92ms

from TreeNode import TreeNode

class Solution_recursive(object):
    def __init__(self):
        # maintain global state so each revcursive call can acess and modify the current total sum
        self.total = 0
    def convertBST(self,root):
        if root == None: return root
        if root.right != None:
            self.convertBST(root.right)
        self.total += root.val
        root.val = self.total
        if root.left != None:
            self.convertBST(root.left)
        return root

# Solution 2 Interation with a stack 92ms

class Solution_Iteration_Stack(object):
    def convertBST(self, root):
        if root == None: return root
        stack = []
        total = 0
        node = root
        while node or len(stack) != 0:
            # push all right nodes to the stack
            while node:
                stack.append(node)
                node = node.right
            
            node = stack.pop()
            total += node.val
            node.val = total

            node = node.left
            
        return root
            
# Solution 3 Morris Traversal 96ms
class Solution(object):
    def convertBST(self,root):
        #Get the node with the smallest value greater than this one
        # Its right child's leftmost grandchild
        def get_successor(node):
            succ = node.right
            while succ.left is not None and succ.left is not node:
                succ = succ.left
            
            return succ

        total = 0
        node = root
        while node is not None:
            # If there is no right subtree, then we can visit this node and continue traversing left.
            if node.right is None:
                total += node.val
                node.val = total
                node = node.left
            
            # If this is a right subtree then there is a node that
            #has a greater value than the current one. therefore, we must 
            # traversal that node fist.
        
            else:
                succ = get_successor(node)
                # If this is no left subtree( or right subtree, becuase we are in
                # this branch of contreol flow), make a temporary connection 
                # back to the current node.
                if succ.left is None:
                    succ.left = node
                    node = node.right
                
                # If there is a left subtree, it is a link that we created
                # on a previous pass, so we should unlink it and visit this node.

                else:
                    succ.left = None
                    total += node.val
                    node.val = total
                    node = node.left
        return root


t20 = TreeNode(20)
t10 = TreeNode(10)
t30 = TreeNode(30)
t5 = TreeNode(5)
t11 = TreeNode(11)
t25 = TreeNode(25)
t35 = TreeNode(35)
t7 = TreeNode(7)
t12 = TreeNode(12)
t28 = TreeNode(28)
t6 = TreeNode(6)

t20.left = t10
t20.right = t30
t10.left = t5
t10.right = t11
t30.left = t25
t30.right = t35
t5.right = t7
t11.right = t12
t25.right = t28
t7.left = t6

obj = Solution()
res = obj.convertBST(t20)


