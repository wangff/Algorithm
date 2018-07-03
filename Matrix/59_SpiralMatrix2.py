class Solution(object):
    def generateMatrix(self,n):
        if n == 0: return []

        ans = [[0]*n for _ in range(n)]

        dr = [0,1,0,-1]
        dc = [1,0,-1,0]
        r = c = di = 0

        for i in range(n*n):
            ans[r][c] = i+1
            cr, cc = r+dr[di], c+dc[di]
            if 0<=cr<n and 0<=cc<n and ans[cr][cc]== 0:
                r,c = cr,cc
            else:
                di = (di+1)%4
                r,c = r+dr[di],c+dc[di]
        
        return ans

obj = Solution()
res = obj.generateMatrix(3)
print(res)

        