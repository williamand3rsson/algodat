import copy

class Util:
    @staticmethod
    def closest(Px, Py, n):

        ##divide
        mid = n//2
        if(n==2): return Px[0].distanceTo(Px[1])
        if(n==3): 
            return min(Px[0].distanceTo(Px[1]), Px[0].distanceTo(Px[2]), Px[2].distanceTo(Px[1]))
        Lx = Px[:int(mid)]
        Rx = Px[int(mid):]
        Ly = sorted(Lx, key=lambda node: node.y)
        Ry = sorted(Rx, key=lambda node: node.y)
        delta = min(Util.closest(Lx, Ly, mid), Util.closest(Rx, Ry, mid))

        ##combine
        S = []  
        for yPoint in Py:
            if yPoint.x < delta + Px[mid].x and yPoint.x > Px[mid].x - delta:
                S.append(yPoint)
        n = len(S)
        for i in range(n):
            for j in range(i+1, min(i+8, n)): 
                delta = min(delta, S[i].distanceTo(S[j]))
        return delta
   
            
        
