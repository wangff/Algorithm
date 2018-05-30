# 438. Find All Anagrams in a String
# Sliding window approach
import collections
class Solution(object):
    def findAnagrams(self,s,p):

        res = []
        pDict = collections.Counter(p)

        left = right = 0
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
                if s[left] in pDict:
                    pDict[s[left]] += 1
                    if pDict[s[left]] > 0:
                        count += 1
                    if right - left == lengthP: res.append(left)
                    
                # Once the window's is greater than p's size, we move left to keep sure the windows's size is equal to p's size
                left += 1

        return res

obj = Solution()
res = obj.findAnagrams("abab","ab")
print(res)