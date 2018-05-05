# Solution 1: using the general Union-Find methond
# explanation:
# Union a virtual root with any "O" on the border and any "O" that could be connected to an "O" on the border
# Then change all of "O" that can't be connected to the border to "X"

from Quick_Union import QuickUnionUf
class Solution_UnionFind (object):
    def solve(self, board):
        if board == None or len(board) == 0 or len(board[0])==0: return
        rows = len(board)
        colums = len(board[0])
        virtualRoot = rows*colums
        quickUF = QuickUnionUf(virtualRoot+1)

        for i in range(rows):
            for j in range(colums):
                if board[i][j] == "X": continue
                curr = i*colums + j
                if i in (0,rows-1) or j in (0,colums-1):
                    quickUF.union(curr,virtualRoot)
                else:
                    if j+1 < colums and board[i][j+1] == "O":
                        quickUF.union(curr, i*colums+j+1)
                    if j-1 >= 0 and board[i][j-1]=="O":
                        quickUF.union(curr, i*colums+j-1)
                    if i+1 < rows and board[i+1][j] == "O":
                        quickUF.union(curr,(i+1)*colums+j)
                    if i-1 >= 0 and board[i-1][j] == "O":
                        quickUF.union(curr,(i-1)*colums+j)
        
        for i in range(rows):
            for j in range(colums):
                curr = i*colums + j
                if board[i][j]=="O" and not quickUF.connected(curr,virtualRoot):
                    board[i][j] = "X"


# Solution 2 Using BFS

class Solution_BFS(object):
    def solve(self,board):
        if not any(board): return
        rows, colums = len(board), len(board[0])

        # save the border elements
        save = set([ij for k in range(max(rows,colums)) for ij in ((0,k),(rows-1,k),(k,0),(k,colums-1))])

        while save:
            i,j = save.pop()
            if 0<=i<rows and 0<=j<colums and board[i][j] == "O":
                board[i][j] = "S"
                save |= set([(i,j-1),(i,j+1),(i-1,j),(i+1,j)])
        
        board[:] = [['XO'[elem=='S'] for elem in row] for row in board]


