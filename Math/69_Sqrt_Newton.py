class Solution(object):
    def mySqrt(self,a):
        x = a
        while x*x > a:
            x = (x+a/x)/2
        return x

my_s = Solution()
result = my_s.mySqrt(4)
print(result)