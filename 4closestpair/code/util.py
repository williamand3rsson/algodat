class Util:

    def closest(Px, Py, n):
        mid = n/2
        Lx = Px[:mid]
        Rx = Px[mid:]
        Ly = Py[:mid]
        Ry = Py[mid:]
        delta = min(closest(Lx, Ly, n/2), closest(Rx, Ry, n/2))
        #Sy = ???


    def closestPoint(points):
        Px = []
        Py = []
        for point in points:
            Px.append(point.x)
            Py.append(point.y)
        Px.sort()
        Py.sort()
        print(Px, Py)
        closest(Px, Py, len(points))

    

#Sorterar Px och Py samt anropar closest
   
            
        
