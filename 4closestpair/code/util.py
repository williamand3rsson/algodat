import copy

class Util:

    def closest(Px, Py, n):
        mid = n/2
        if(n==2): return Px[0].distanceTo(Py[1])
        if(n==3): 
        Lx = Px[:mid]
        Rx = Px[mid:]
        Ly = Py[:mid]
        Ry = Py[mid:]
        delta = min(closest(Lx, Ly, n/2), closest(Rx, Ry, n/2))
        #Sy = ???


    def closestPoint(points):
        Px = points[:]
        Py = points[:]
        Px.sort(key=points.x)
        Py.sort(key=points.y)
        print(Px, Py)
        closest(Px, Py, len(points))

    

#Sorterar Px och Py samt anropar closest
   
            
        
