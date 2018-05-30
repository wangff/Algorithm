# Python Sliding window approach to solve substring search problem from easy to hard

## References

1.  https://leetcode.com/problems/find-all-anagrams-in-a-string/discuss/92007/Sliding-Window-algorithm-template-to-solve-all-the-Leetcode-substring-search-problem.
2.  https://leetcode.com/problems/minimum-window-substring/discuss/26808/Here-is-a-10-line-template-that-can-solve-most-'substring'-problems
3.  https://leetcode.com/problems/substring-with-concatenation-of-all-words/discuss/13656/An-O(N)-solution-with-detailed-explanation

Thanks to brilliant approaches and comprehensive summary from above articles, I could have an in-depth understanding of sliding window algorithm. 
 
## Why do I have to write this article

1. Since I have spent several hours to figure out the code from above articles, I would like to record the process of thinking, and provide other readers another perspective to understand this algorithm.
2. Since the same algorithm or code template could be used in solving several different, I would like to the implementation of this template in different problems is as similar as possible. I think, in this way, it's much more easy to figure out the algorithm.
3. I code in Python, and want to make my code more Pythonic.

## Typical problems

1.  [438. Find All Anagrams in a String]([](https://leetcode.com/problems/find-all-anagrams-in-a-string/description/)): Given a string s and a non-empty string p, find all the start indices of p's anagrams in s. Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100. The order of output does not matter.
    1. Input: s: "cbaebabacd" p: "abc"; Output: [0, 6]
    2. Input: s: "abab" p: "ab"; Output: [0, 1, 2]
2.  [30. Substring with Concatenation of All Words](https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/): You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.
    1.  Input: s = "barfoothefoobarman", words = ["foo","bar"]; 
        Output: [0,9]
    2.  Input: s = #"wordgoodgoodgoodbestword",                                         
        words=["word","good","best","good"]; 
        Output: [8]
    3.  Input: s = #"wordgoodgoodgoodbestword",                                         
        words=["word","good","best","word"]; 
        Output: []
    4.  Input: "aaaaaaaa", words=["aa","aa","aa"]
        Output: [0,1,2]
3.  Differences between problem 438 and problem 30
    1. The smallest element in 438 is character, while the smallest element in 30 is a word in words. Therefore, the loop increment in 438 is 1 (`right += 1; left += 1`), while the loop increment in 30 the length of word (`right += wordLen; left += wordLen`)
    2.  Considering the input ("aaaaaaaa", words=["aa","aa","aa"]), if we increment the right or left boundary by the length of word (which is 2) in each loop, we just has two substring that meets the requirements: s[0:6] and s[2:8]. However, the substring s[1:7] also meet the requirement, but we miss it. Why? Since we have (`right += wordLen; left += wordLen`) in each loop, so we inevitably skip the 'a' character at s[1]. Therefore, compared to the code of 438, we need an extra outside loop in 30 to calculate the characters we have skipped. The length of this outside loop is the length of word, because the number of skipped characters is equal to the length of word.
    
    Actually, apart from the above differences, those two problem is exactly same.

438.Find All Anagrams in a String

```

import collections
class Solution(object):
    def findAnagrams(self,s,p):
        res = []
        lengthS, lengthP = len(s), len(p)
        if lengthS==0 or lengthP==0: return res
        pDict = collections.Counter(p)
        
        left = right = 0
        count = lengthP
        
        while right < lengthS:

            # move right everytime, if the character exists in p's hash, decrease the count
            # current hash value >=1 means the character is exisitng in P
            ch = s[right]
            if ch in pDict:
                pDict[ch] -= 1
                # current hash value >=1 means the character is exisitng in P
                # Maybe p just has two 's', but we meet tree 's' when traversing
                if pDict[ch]>=0:
                    count -= 1
            right += 1
        

            # if we find the window whose size equals to p, then we move left ( narrow the window ) to find the new match window
            # reset the hash because we kicked out the left
            # only increase the count if the character is in P
            
            ch = s[left]
            while count == 0:
                if ch in pDict:
                    pDict[ch] += 1
                    if pDict[ch] > 0:
                        count += 1
                    if right - left == lengthP: res.append(left)
                    
                # Once the window's is greater than p's size, we move left to keep sure the windows's size is equal to p's size
                left += 1

        return res

```

30.Substring with Concatenation of All Words

```
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
        
```

