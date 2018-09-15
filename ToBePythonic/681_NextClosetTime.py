#Solution 1 Simulation
class Solution_simulation(object):
    def nextClosestTime(self,time):
        # change 11:39 to minutes
        cur = int(time[0:2])*60+int(time[3:])

        # legal digits
        allowed = {int(ch) for ch in time if ch!=":"}

        # going forwad the time by 1 minute
        while True:
            cur = (cur+1)%(60*24)
            if all(digit in allowed 
                    for block in divmod(cur,60)
                        for digit in divmod(block,10)):
                return "{:02d}:{:02d}".format(*divmod(cur,60))

import itertools
#Solution2 Build from allowed digits
class Solution(object):
    def nextClosestTime(self,time):
        ans = start = int(time[0:2])*60+int(time[3:])

        allowed = {int(x) for x in time if x!=":"}

        maxElapsed = 24*60

        for h1,h2,m1,m2 in itertools.product(allowed,repeat=4):
            hours,mins = h1*10+h2,m1*10+m2
            if hours<24 and mins<60:
                cur = hours*60+mins
                candElapsed = (cur-start)%(24*60)
                if 0<candElapsed<maxElapsed:
                    ans = cur
                    maxElapsed = candElapsed

        return "{:02d}:{:02d}".format(*divmod(ans,60))


obj = Solution()
res = obj.nextClosestTime("23:59")
print(res)
