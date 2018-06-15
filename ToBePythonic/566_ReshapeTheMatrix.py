# 56 reshape the matrix

# Solution 1: numpy reshape method
# 160 ms
import numpy as np
class Solution_1(object):
    def matrixReshape(self,nums,r,c):
        try:
            res = np.reshape(nums,(r,c)).tolist()
            return res
        except:
            return nums

# Solution 2: flat and zip
class Solution_2(object):
    def matrixReshape(self,nums,r,c):
        flat = sum(nums,[])
        if len(flat) != r * c:
            return nums
        it = [iter(flat)]*c
        tuples = zip(*it)
        return list(map(list,tuples))
        

# Solution 3: itertools 
# 96ms
import itertools
class Solution_3(object):
    def matrixReshape(self,nums,r,c):
        if r*c != len(nums)*len*(nums[0]):
            return nums
        flat = itertools.chain.from_iterable(nums)
        res = [list(itertools.islice(flat,c)) for _ in range(r)]
        return res


# Solution 4: Array index
class Solution(object):
    def matrixReshape(self,nums,r,c):
        if r*c != len(nums)*len(nums[0]):
            return nums
        res = [[0]*c for _ in range(r)]
        count = 0
        for row in nums:
            for val in row:
                res[count//c][count%c]=val
                count += 1
        
        return res 

obj = Solution()
res = obj.matrixReshape([[1,2],[3,4]],1,4)
print(res)