class Node:

    def __init__(self, name):
        self.name = name
        self.edges = []

    def addEdge(self, newEdge):
        self.edges.append(newEdge)

    def __str__(self):
        return f"{self.name}"
    