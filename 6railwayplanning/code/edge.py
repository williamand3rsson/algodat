class Edge:
    def __init__(self, c):
        self.c = c
        self.flow = 0
        cap = 0
        
    def updateCap(self):
        self.cap = self.c - self.flow 
    


    