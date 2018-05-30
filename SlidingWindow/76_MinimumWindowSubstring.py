# 76 Minimum window substring

import collections
import sys
class Solution(object):
    def minWindow(self,s,p):

        res = sys.maxsize
        pDict = collections.Counter(p)

        left = right = head = 0
        lengthP = count = len(p)
        lengthS = len(s)

        while right < lengthS:

            # move right everytime, if the character exists in p's hash, decrease the count
            # current hash value >=1 means the character is exisitng in P
          
            if s[right] in pDict:
                pDict[s[right]] -= 1
                # current hash value >=1 means the character is exisitng in P
                # might be p just has two 's', but we meet tree 's' when traversing
                if pDict[s[right]]>=0:
                    count -= 1
            right += 1
        
            # if we find the window whose size equals to p, then we move left ( narrow the window ) to find the new match window
            # reset the hash because we kicked out the left
            # only increase the count if the character is in P
            while count == 0:

                # move left, narrow the windows.
                # if the new window still contain p, update the shortest substring.
                if right-left < res:
                    head = left
                    res = right - left
                # move left, narrow the windows
                # untill the new window can't have all of characters in P
                if s[left] in pDict:
                    pDict[s[left]] += 1
                    if pDict[s[left]] > 0:
                        count += 1
                left += 1

        return s[head:head+res] if res!=sys.maxsize else ""

obj = Solution()
res = obj.minWindow("ADOBECODEBANC","ABC")
print(res)
