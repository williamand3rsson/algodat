class Nodes:
    def __init__(self, name):
        self.name = name
        self.neighbour = []
        self.visited = False
        self.pred = None

    def addNb(self, node):
        self.neighbour.append(node)