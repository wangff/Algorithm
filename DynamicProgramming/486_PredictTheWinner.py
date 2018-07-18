# Approach #1 Using Recursion
# Time Limited Exceed
class Solution_Rec(object):
    def PredictTheWinner(self,nums):
        return self.helper(nums,0,len(nums)-1,1)>=0
    
    def helper(self,nums,s,e,turn):
        if s==e:
            return turn*nums[s]
        a =turn*nums[s]+self.helper(nums,s+1,e,-1*turn)
        b =turn*nums[e]+self.helper(nums,s,e-1,-1*turn)
        return turn*max(turn*a,turn*b)

# Approach # 2 Using Recursion with memory
class Solution_Rec_Memo(object):
    def PredictTheWinner(self,nums):
        memory = [[0]*len(nums) for _ in range(len(nums))]
        return self.helper(nums,0,len(nums)-1, memory)>=0
    def helper(self,nums,s,e,memory):
        if s==e:
            return nums[s]
        if memory[s][e] != 0:
            return memory[s][e]
        a = nums[s] - self.helper(nums,s+1,e,memory)
        b = nums[e] - self.helper(nums,s,e-1,memory)

        memory[s][e] = max(a,b)
        return memory[s][e]

# Approach #3 Dynamic Programming with 2-D Memory
class Solution_DP_2D(object):
    def PredictTheWinner(self,nums):
        dp = [[0]*len(nums) for _ in range(len(nums)+1)]
        for s in range(len(nums)-2,-1,-1):
            for e in range(s+1,len(nums)):
                a = nums[s]-dp[s+1][e]
                b = nums[e]-dp[s][e-1]
                dp[s][e] = max(a,b)
        
        return dp[0][len(nums)-1]>=0

# Appraoch #4 Dyanmic Programming with 1-D Memory
# Keep the row
class Solution(object):
    def PredictTheWinner(self,nums):
        dp = [0]*len(nums)
        for s in range(len(nums)-2,-1,-1):
            for e in range(s+1,len(nums)):
                a = nums[s]-dp[e]
                b = nums[e]-dp[e-1]
                dp[e] = max(a,b)
        
        return dp[len(nums)-1] >=0 
obj = Solution()
res = obj.PredictTheWinner([1,5,233,7])
print(res)