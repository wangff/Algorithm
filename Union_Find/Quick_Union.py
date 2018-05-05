# explanation
#https://www.youtube.com/watch?v=H0bkmI1Xsxg&list=PLe-ggMe31CTexoNYnMhbHaWhQ0dvcy43t&index=3

class QuickUnionUf:
    id = []
    sz = []
    def __init__(self, n):
        self.id = [i for i in range(n)]
        self.sz = [1]*n
    
    # find the root parent
    def root(self,i):
        while i!=self.id[i]: 
            # flatten the tree
            # make every node in path point to its grandparent
            self.id[i] = self.id[self.id[i]] 
            i = self.id[i]
        return i
    
    # check if two item is connected
    def connected(self,p,q):
        return self.root(p)==self.root(q)
    
    # union two item
    # Weighted Quick Union
    def union(self,p,q):
        i = self.root(p)
        j = self.root(q)
        if i == j: return
        if self.sz[i] < self.sz[j]:
            self.id[i] = j
            self.sz[j] += self.sz[i]
        else:
            self.id[j] = i
            self.sz[i] += self.sz[j]


obj = QuickUnionUf(16)