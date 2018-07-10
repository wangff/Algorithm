# Solution #1 Dynamic Programming
class Solution_DP(object):
    def integerBreak(self,n):
        dp = [0]*(n+1)
        dp[0]=1
        dp[1]=1
        for i in range(1,n+1):
            for j in range(i):
                if i-j==n: continue
                dp[i] = max(dp[i],(i-j)*dp[j])
        
        return dp[n]

# Solution # 2 Math
class Solution(object):
    def integerBreak(self,n):
        if n==2 or n==3:
            return n-1
        res = 1
        while n > 4:
            n -= 3
            res *=3
        return n*res
obj = Solution()
res = obj.integerBreak(10)
print(res)

