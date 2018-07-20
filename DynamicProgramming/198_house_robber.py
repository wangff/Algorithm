class Solution(object):
    def rob(self, nums):
        ifpreNotRobbed = 0
        ifpreRobbed = 0
        for i in nums:
            curRobbed = ifpreNotRobbed + i
            curNotRobbed = max(ifpreNotRobbed,ifpreRobbed)

            ifpreNotRobbed = curNotRobbed
            ifpreRobbed = curRobbed
        
        return max(ifpreNotRobbed,ifpreRobbed)

my_s = Solution()
result = my_s.rob([2,3])