from queue import PriorityQueue    
class Multiway_Merge(object):
    def merge(self, vector):
        S = []

        PQ = PriorityQueue()

        for i in range(len(vector)):
            if len(vector[i])!=0:
                PQ.put(vector[i])
        
        while not PQ.empty():
            R = PQ.get()
            S.append(R[0])
            if len(R)!=1:
                PQ.put(R[1:])


        return S

if __name__ == '__main__':
    data = [[1,2,3],[],[4,5,6],[3,4,6,8]]
    obj = Multiway_Merge()
    res = obj.merge(data)
    print(res)