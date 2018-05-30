from collections import Counter
class Solution(object):
    def subarraySum(self,nums,k):
        count = 0
        currSum = 0
        prefixSumHash = Counter()
        prefixSumHash[0] = 1

        for num in nums:
            currSum += num
            startPos = currSum - k
            count += prefixSumHash[startPos]
            prefixSumHash[currSum] += 1
     
      
        return count
        
obj = Solution()
res = obj.subarraySum([1,1,1],2)
print(res)