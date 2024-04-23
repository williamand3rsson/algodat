from node import Node
from collections import deque

class BFS:        

    def algorithm(start, end, nodeList, wordLib):
        predList = []
        qList = deque([(start, 1)])
        currentNode = None
        

        for n in nodeList.values():
            n.visited = 0
        start.visited = 1

        if(start.name == end.name):
            print("0")
            return

        while len(qList) != 0:
            currentNode, distance = qList.popleft()
            if(len(currentNode.neighbourList) == 0):
                currentNode.findNeighbour(wordLib)
            for nb in currentNode.neighbourList:
                nb = nodeList[nb]
                if nb.visited != 1:
                    nb.visited = 1
                    qList.append((nb, distance + 1))
                    nb.pred = currentNode
                    if(nb.name == end.name):
                        print(distance)
                        return
        print("Impossible")

# 5large1 - 30s algoritm, 8s inläsning
# 6large2 - 18s algoritm, 8s inläsning

# 5large1 - 25s
# 6large2 - 19s