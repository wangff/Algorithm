# Sotion 1 layer by layer with Generator
class Solution1(object):
    def spiralOrder(self,matrix):
        def spiral_coords(r1,c1,r2,c2):
            for c in range(c1, c2+1):
                yield r1, c
            for r in range(r1+1,r2+1):
                yield r, c2
            
            if r1 < r2 and c1 < c2:
                for c in range(c2-1,c1,-1):
                    yield r2, c
                for r in range(r2, r1, -1):
                    yield r, c1
        
        if not matrix: return []
        ans = []
        r1,r2 = 0, len(matrix)-1
        c1,c2 = 0, len(matrix[0])-1

        while r1<=r2 and c1<=c2:
            for r,c in spiral_coords(r1,c1,r2,c2):
                ans.append(matrix[r][c])
            r1+=1
            r2-=1
            c1+=1
            c2-=1
        return ans


#Solution 2 clockwise
class Solution(object):
    def spiralOrder(self,matrix):
        if not matrix: return []
        R,C = len(matrix), len(matrix[0])
        visited = [[False]*C for _ in range(R)]
        ans = []
        dr = [0,1,0,-1]
        dc = [1,0,-1,0]
        r = c = di = 0

        for _ in range(R*C):
            ans.append(matrix[r][c])
            visited[r][c] = 1
            cr, cc = r+dr[di], c+dc[di]
            if 0<=cr<R and 0<=cc<C and not visited[cr][cc]:
                r , c = cr, cc
            else:
                di = (di+1)%4
                r,c = r+dr[di],c+dc[di]
        return ans

matrix = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
obj = Solution()
res = obj.spiralOrder(matrix)
print(res)