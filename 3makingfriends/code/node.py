from queue import PriorityQueue

class Node:

    def __init__(self, name):
        self.name = name
        self.edges = PriorityQueue()

    def addEdge(self, prio, nb):
        self.edges.put(prio, (nb, prio))

    def __str__(self):
        return f"{self.name}"
    