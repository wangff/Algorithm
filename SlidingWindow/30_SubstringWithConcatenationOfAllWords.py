import collections
class Solution(object):
    def findSubstring(self,s,p):
        res = []
        lengthS, lengthP = len(s), len(p)
        if lengthS==0 or lengthP==0: return res
        pDict = collections.Counter(p)
        wordLen = len(p[0])
        totalLen = lengthP * wordLen
        # Why we need this outside loop?
        # Considering the example input: Input: "aaaaaaaa", words=["aa","aa","aa"]
        # See the explanantion of 3.2 under the tile typical problem
        for i in range(wordLen):

            # Everytime we calculate from a new start point, we need a totally new initialization.
            # We would't like to change the original pDict after each calculating
            # So we make a new copy and seed this new copy instead of the original pDict to the auxiliary method
            tmpDict = dict(pDict)
            self.slidingWindow(s,tmpDict,totalLen,wordLen,i,lengthP,lengthS,res)
        return sorted(res)
       

    # This auxiliary method is the same as the code of problem 438 
    def slidingWindow(self,s,pDict,totalLen,wordLen,start,lengthP,lengthS,res):
        left = right = start
        count = lengthP
        while right <= lengthS - wordLen:
            word = s[right:right+wordLen]
            if word in pDict:
                pDict[word] -= 1
                if pDict[word] >= 0:
                    count -= 1
            right += wordLen


            while count == 0:
                word = s[left:left+wordLen]
                if word in pDict:
                    pDict[word] += 1
                    if pDict[word] > 0:
                        count += 1
                    if right - left == totalLen: res.append(left)
                
                left += wordLen
                

        return res


#"wordgoodgoodgoodbestword"
#["word","good","best","word"]
# "aaaaaa"
# ["aa","aa","aa"]
obj = Solution()
res = obj.findSubstring("wordgoodgoodgoodbestword",["word","good","best","good"])
print(res)