class MajorityNumber(object):
    def findMajorityNumber(self,A):
        cnt = 0
     
        for x in A:
            if cnt == 0: # there is no element in pool
                mrk = x
                cnt += 1  # put the current char in pool
            else:
                if mrk == x: # the current char is the same with the char in pool
                    cnt += 1 # still put this char in pool
                else: # the current char is not the same with the char in pool
                    cnt -= 1 # elimante the current char and one char from the pool
        
        if cnt == 0: # there is no char in the pool
            return False
        
        cnt = sum([1 for x in A if x ==mrk])

        return mrk if 2*cnt >= len(A) else False

obj = MajorityNumber()
res = obj.findMajorityNumber(['a','b'])
print(res)

