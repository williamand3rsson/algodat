class Nodes:
    def __init__(self, name):
        self.name = name
        self.neighbour = []
        self.visited = 0

    def addNb(self, node):
        self.neighbour.append(node)