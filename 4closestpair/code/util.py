import copy

class Util:
    @staticmethod
    def closest(Px, Py, n):
        mid = n//2
        if(n==2): return Px[0].distanceTo(Px[1])
        if(n==3): 
            return min(Px[0].distanceTo(Px[1]), Px[0].distanceTo(Px[2]), Px[2].distanceTo(Px[1]))
        Lx = Px[:int(mid)]
        Rx = Px[int(mid):]
        Ly = sorted(Lx, key=lambda node: node.y)
        Ry = sorted(Rx, key=lambda node: node.y)
        delta = min(Util.closest(Lx, Ly, mid), Util.closest(Rx, Ry, mid))
        S = []
        #i = len(Lx) -1
        # while Lx[i].x > -(delta) + Px[mid].x and len(S) != len(Lx):
        #     print(i)
        #     S.append(Lx[i])
        #     i -= 1
        # j = 0
        # while Rx[i].x <= (delta) + Px[mid].x:
        #     S.append(Lx[i])
        #     j += 1
            
        for yPoint in Py:
            if yPoint.x < delta + Px[mid].x and yPoint.x > Px[mid].x - delta:
                S.append(yPoint)
        n = len(S)
        for i in range(n):
            for j in range(i+1, min(i+8, n)):  # Start from i+1 to avoid testing the same pair again
                delta = min(delta, S[i].distanceTo(S[j]))
        return delta
        #Sy = ???


    # def closestPoint(self, points):
    #     Px = points[:]
    #     Py = points[:]
    #     Px = sorted(points, key=lambda node: node.x)
    #     Py = sorted(points, key=lambda node: node.y)
    #     print(Px, Py)
    #     self.closest(Px, Py, len(points))

    

#Sorterar Px och Py samt anropar closest
   
            
        
