# If we "take" a number (use it to score points),
# we as well take all copies of it,
# since we've already erased all its neighbors.


import collections
class Solution(object):
    def deleteAndEarn(self,nums):
        cntDict = collections.Counter(nums)
        prevKey = None
        ifPreSelected = 0
        ifPreNotSelected = 0
        
        for key in reversed(sorted(cntDict.keys())):
            # key!=prevKey+1
            # No matter prevKey is selected or not Selected; key could be selected.
            # key could be selected
            if key+1!= prevKey:
                curSelected = key*cntDict[key]+max(ifPreSelected,ifPreNotSelected)
                curNotSelected = max(ifPreNotSelected,ifPreSelected)
            else: 
                # key==prevKey-1
                # Only if prevKey is not selected, key could be selected
                # If prevKey is selected, key could not be selected
                curSelected = ifPreNotSelected + key*cntDict[key]
                curNotSelected = max(ifPreNotSelected,ifPreSelected)

            prevKey = key
            ifPreNotSelected = curNotSelected
            ifPreSelected = curSelected
        
        return max(ifPreNotSelected,ifPreSelected)
            
obj = Solution()
res = obj.deleteAndEarn([2, 2, 3, 3, 3, 4])
print(res)




