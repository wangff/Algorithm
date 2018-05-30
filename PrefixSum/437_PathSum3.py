from TreeNode import TreeNode
# Solution 1 preorder traversal 1088ms
class Solution_preorder(object):
    def pathSum(self, root, summ):

        if root == None: return 0

        cur = self.pathSumFromRoot(root,0,summ)
        left = self.pathSum(root.left,summ)
        right = self.pathSum(root.right,summ)

        return cur + left + right

    def pathSumFromRoot(self,root,prefixsum,summ):
        if root == None: return 0
        currsum = prefixsum + root.val
        cur = int(currsum == summ)
        left = self.pathSumFromRoot(root.left,currsum,summ)
        right = self.pathSumFromRoot(root.right,currsum,summ)
        return cur + left + right

# Solution 2 prefix sum  64ms
class Solution(object):
    def __init__(self):
        self.count = 0

    def pathSum(self,root,summ):
        if root == None: return 0

        self.prefixSum(root,0,summ,{0:1})

        return self.count
    
    def prefixSum(self,root,prefixSum,target, prefixSumHash):

        if root == None: return

        currSum = prefixSum + root.val

        startPos = currSum - target
        
        if startPos in prefixSumHash.keys():
            self.count += prefixSumHash[startPos]

        prefixSumHash.setdefault(currSum,0)
        prefixSumHash[currSum] += 1
        
        self.prefixSum(root.left,currSum,target,prefixSumHash)
        self.prefixSum(root.right,currSum,target,prefixSumHash)

        prefixSumHash[currSum] -= 1 


        


# t10 = TreeNode(10)
# t5 = TreeNode(5)
# t_3 = TreeNode(-3)
# t3 = TreeNode(3)
# t2 = TreeNode(2)
# t11 = TreeNode(11)
# t33 = TreeNode(3)
# t_2 = TreeNode(-2)
# t1 = TreeNode(1)

# t10.left = t5
# t10.right = t_3
# t5.left = t3
# t5.right = t2
# t3.left = t33
# t3.right = t_2

# t2.right = t1

# t_3.right = t11

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(-1)
n4 = TreeNode(-1)
n5 = TreeNode(2)

n1.left = n2
n2.left = n3
n3.left = n4
n4.left = n5

obj = Solution()
res = obj.pathSum(n1,2)
print(res)