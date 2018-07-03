import queue
class Huffman(object):
    def calculatHuffman(self, P):
        first = second = float()
        F = []

        while len(P) +  len(F) > 1:
            if len(P) !=0 and len(F)!=0:
                if P[0] < F[0]:
                    first = P[0]
                    del(P[0])
                else:
                    first = F[0]
                    del(F[0])
            else:
                if len(F)==0:
                    first = P[0]
                    del(P[0])
                else:
                    first = F[0]
                    del(F[0])
            
            if len(P) !=0 and len(F)!=0:
                if P[0] < F[0]:
                    second = P[0]
                    del(P[0])
                else:
                    second = F[0]
                    del(F[0])
            else:
                if len(F)==0:
                    second = P[0]
                    del(P[0])
                else:
                    second = F[0]
                    del(F[0])
            F.append(first + second)

obj = Huffman()
res = obj.calculatHuffman([0.0625,0.0625,0.0625,0.0625,0.125,0.125,0.125,0.125,0.25])

