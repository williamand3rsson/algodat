from node import Node
from collections import deque

class BFS:
        
    def algorithm(start, end, nodeList):
        predList = []
        qList = deque([(start, [start])])  
        currentNode = None
        
        for n in nodeList.values():
            n.visited = 0
        start.visited = 1

        while len(qList) != 0:
            currentNode, path = qList.popleft()
            for nb in currentNode.neighbourList:
                nb = nodeList[nb]
                if nb.visited != 1:
                    nb.visited = 1
                    qList.append((nb, path + [nb]))  
                    nb.pred = currentNode
                    if nb.name == end.name:
                        return path + [end] 
        return None  

