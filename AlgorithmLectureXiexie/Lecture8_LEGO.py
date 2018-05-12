class Floor(object):
    def __init__(self,n):
        self.N = 2**n
        self.floor = [[0 for _ in range(self.N)] for _ in range(self.N)]
        self.f = open("result.txt","a+")
    
    def coverCurrentSpot(self,spot,label):
        self.floor[spot[0]][spot[1]] = label

    def getLabelofSpot(self,spot):
        return self.floor[spot[0]][spot[1]]

    def printFloor(self,label):
        self.f.write("Put the brick number "+str(label)+"\n")
        for row in self.floor:
            self.f.write(str(row)+"\n")

class LEGO(object):
    def __init__(self,n):
        self.label = 1
        self.floor = Floor(n)
    # start: the top left corner
    # spot: the initial covered spot
    def solveLEGE(self,N,start,spot):
        # termination condition
        if N <=1: return

        # Divide the problem to subproblem
        # The side of floor is divided by 2
        # The floor is divided by 4 just like quadrants of Cartesian plain
        # So the problem is divided by 4
        half = N//2

        # Every subfloor should has a spot that has been already covered
        # So there are four spots that shuld be covered before entering the subproblem
        
        # One of them is the covered spot from parent floor
        # The left three is what we are going to cover by using a LEGO L brick
      
        spots4sub = [[(0,0),(0,0)],[(0,0),(0,0)]]
        
        # The covered spot in 1st quadrant, the right bottom of the 1st quadrant
        spots4sub[0][0] = (start[0] + half - 1, start[1]+half-1)
        # The covered spot in 2st quadrant, the left bottom of the 2st quadrant
        spots4sub[0][1] = (start[0] + half - 1, start[1]+half)
        # The covered spot in 3st quadrant, the right upper of the 3st quadrant
        spots4sub[1][0] = (start[0] + half, start[1]+half-1)
        # The covered spot in 4st quadrant, the left botupper of the 4st quadrant
        spots4sub[1][1] = (start[0] + half, start[1]+half)


        # Recover the orignal covered spot

        p = (spot[0]-start[0])//half
        q = (spot[1]-start[1])//half

        spots4sub[p][q] = spot

        # Temporarily keep the value of current covered spot
        temp = self.floor.getLabelofSpot(spots4sub[p][q])

        # Put a brick on sports4sub
        self.floor.coverCurrentSpot(spots4sub[0][0], self.label)
        self.floor.coverCurrentSpot(spots4sub[0][1], self.label)
        self.floor.coverCurrentSpot(spots4sub[1][0], self.label)
        self.floor.coverCurrentSpot(spots4sub[1][1], self.label)

        # Recove the spot that has been covered before
        self.floor.coverCurrentSpot(spots4sub[p][q],temp)

        self.floor.printFloor(self.label)

        self.label += 1

        #Recursively solve four subproblems
        self.solveLEGE(half,start,spots4sub[0][0])
        self.solveLEGE(half,(start[0],start[1]+half),spots4sub[0][1])
        self.solveLEGE(half,(start[0]+half,start[1]),spots4sub[1][0])
        self.solveLEGE(half,(start[0]+half,start[1]+half),spots4sub[1][1])

if __name__ == '__main__':

    n = 3

    lego = LEGO(n)

    lego.solveLEGE(2**n,(0,0),(4,7))

