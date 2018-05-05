# Solution 1: using the general Union-Find methond
# explanation:
# Union all of adjanet "1"
# Count the numbers of different roots
from Quick_Union import QuickUnionUf
class Solution(object):
    def numIslands(self,grid):
        if not any(grid): return 0
        rows, colums = len(grid), len(grid[0])
        virtualRoot = rows*colums
        quickUF = QuickUnionUf(virtualRoot+1)
        for i in range(rows):
            for j in range(colums):
                if grid[i][j] == "0": continue
                curr = i*colums + j
                if j+1 < colums and grid[i][j+1] == "1":
                    quickUF.union(curr,i*colums+j+1)
                if j-1 >= 0 and grid[i][j-1] == "1":
                    quickUF.union(curr,i*colums+j-1)
                if i+1 < rows and grid[i+1][j] == "1":
                    quickUF.union(curr,(i+1)*colums+j)
                if i-1 >= 0 and grid[i-1][j] == "1":
                    quickUF.union(curr,(i-1)*colums+j)
        res = []
        for i in range(rows):
            for j in range(colums):
                if grid[i][j]=="1":
                    curr = i*colums + j
                    res += [quickUF.root(curr)]
        return len(set(res))
    
# Solution 2 Using DFS
class Solution_DFS(object):
    def numIslands(self,grid):
        def sink(i,j):
            if 0<=i<len(grid) and 0<=j<len(grid[i]) and grid[i][j]=='1':
                grid[i][j] = '0'
                map(sink,(i+1,i-1,i,i),(j,j,j+1,j-1))
                return 1
            return 0
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                count += sink(i,j)
        
        return count

obj = Solution()
res = obj.numIslands([["1","0","1","1","1"],["1","0","1","0","1"],["1","1","1","0","1"]])
print(res)



   