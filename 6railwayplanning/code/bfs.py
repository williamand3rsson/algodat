from nodes import Nodes
from collections import deque

class BFS:

    @staticmethod        
    def bfs(start, end, nodeList):
        allPaths = []
        qList = deque([(start, [start.name])]) 
        while qList:
            currentNode, path = qList.popleft()
            if currentNode == end:
                allPaths.append(path) 
                continue
            
            for neighbor in currentNode.neighbour:
                neighbor = nodeList[neighbor.name]
                if neighbor.name not in path:  
                    qList.append((neighbor, path + [neighbor.name])) 
        return allPaths