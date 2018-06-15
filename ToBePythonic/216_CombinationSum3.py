#Problem 216. Combination Sum 3
#Find all possible combinations of k numbers that add up to a number n, 
# given that only numbers from 1 to 9 can be used 
# and each combination should be a unique set of numbers.
# Note:
# All numbers will be positive integers.
# The solution set must not contain duplicate combinations.
#Solution 1: My own backtracking approach
class Solution_BT(object):
    def __init__(self):
        self.res = []
        self.visit = [False]*10
    def helper(self,start,k,n,resList):
        if k == 0:
            if n == 0:
                self.res.append(list(resList))
                return False
            elif n <0:
                return False
            else:
                return True
            
        for i in range(start,10):
            if self.visit[i]: continue
            resList.append(i)
            # self.visit[i] = True
            noContinue = self.helper(i+1,k-1,n-i,resList)
            resList.pop()
            # self.visit[i] = False
            if not noContinue: return True
        return True
    def combinationSum3(self,k,n):
        self.helper(1,k,n,[])
        return self.res

# Solution 2: itertools combinations
from itertools import combinations
class Solution_itertools(object):
    def combinationSum3(self,k,n):
        return [c for c in combinations(range(1,10),k) if sum(c)==n]

