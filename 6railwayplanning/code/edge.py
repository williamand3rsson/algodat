class Edge:
    def __init__(self, fromz, to, c):
        self.fromz = fromz
        self.to = to
        self.c = c
        self.flow = 0
    
    def totC(self):
        return self.c - self.flow
    


    