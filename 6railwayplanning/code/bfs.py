from nodes import Nodes
from collections import deque

class BFS:        

    def bfs(start, end, nodeList):
        predList = []
        qList = deque([(start, 1)])
        currentNode = None
        
        for n in nodeList.values():
            n.visited = 0
        start.visited = 1

        while len(qList) != 0:
            currentNode, max = qList.popleft()
            #if(len(currentNode.neighbourList) == 0):
            #    currentNode.findNeighbour(wordLib)
            for nb in currentNode.neighbour:
                nb = nodeList[nb.name]
                if nb.visited != 1:
                    nb.visited = 1
                    qList.append((nb, max + 1))
                    nb.pred = currentNode
                    if(nb.name == end.name):
                        return max
        print("finns ingen väg")