# Collections

## Counter

```
from collections import Counter
class Solution(object):
    def canConstruct(self,ransomNote, magazine):
        ransomCnt = Counter(ransomNote)
        magazineCnt = Counter(magazine)

        for key in ransomCnt:
            if magazineCnt[key] >= ransomCnt[key]:
                continue
            else:
                return False
        
        return True

# To be Pythonic

    def canConstruct_py(self, ransomNote, magazine):
        return not Counter(ransomNote) - Counter(magazine)

```

