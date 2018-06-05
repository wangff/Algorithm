# Lecture 12
# Introduction to Algorithm 4.1 The Maximum Subarray Problem

import sys

# Solution 1: Divide and Conquer
class FindMaxSubarray(object):

    # a linear-time Find-Max-Crossing-Subarray 
    def findMaxCrossing(self,A,low,mid,high):
        left_sum = -sys.maxsize-1
        sum = 0

        # the range is [low, mid)
        max_left = mid-1
        for i in range(mid-1,low-1,-1):
            sum += A[i]
            if sum > left_sum:
                left_sum = sum
                max_left = i
        
        right_sum = -sys.maxsize-1
        sum = 0
        max_right = mid
        # the range is [mid, high)
        for j in range(mid,high):
            sum += A[j]
            if sum > right_sum:
                right_sum = sum
                max_right = j
        
        return (max_left,max_right+1,left_sum+right_sum)
    
    # divide-and-conquer algorithm to solve the maximum suarray proble,
    def findMaximumSubarray(self,A,low,high):
        # the range is [low, high)
        # base case: only one element
        if high == low+1:
            return (low,high,A[low])
        else:
            mid = low+(high-low)//2
            leftTuple = self.findMaximumSubarray(A,low,mid)
            rightTuple = self.findMaximumSubarray(A,mid,high)
            crossTuple = self.findMaxCrossing(A,low,mid,high)

            if leftTuple[2] >= rightTuple[2] and leftTuple[2]>= crossTuple[2]:
                return leftTuple
            elif rightTuple[2] >= leftTuple[2] and rightTuple[2] >= crossTuple[2]:
                return rightTuple
            else:
                return crossTuple
    
    def main(self,P):
        A = [0]*len(P)
        for i in range(1,len(P)):
            A[i] = P[i]-P[i-1]
        
        res = self.findMaximumSubarray(A,1,len(P))
        print(res)


# Solution 2: Kadane's Algorithm
class Kadane(object):
    def findMaximumSubarray(self, A):
        left = right = maxLeft = maxRight = 0
        maxSum = -sys.maxsize-1
        currSum = 0

        for i in range(len(A)):
            currSum += A[i]
            if currSum > maxSum:
                maxSum = currSum
                maxLeft = left
                maxRight = right = i+1
            if currSum < 0:
                currSum = 0
                left = right = i+1

        return (maxLeft,maxRight,maxSum)

    def main(self,P):
        A = [0]*len(P)
        for i in range(1,len(P)):
            A[i] = P[i]-P[i-1]
        
        res = self.findMaximumSubarray(A)
        print(res)
        
P = [100,113,110,85,105,102,86,63,81,101,94,106,101,79,94,90,97]
# P = [10,11,7,10,6]
obj = Kadane()
obj.main(P)




