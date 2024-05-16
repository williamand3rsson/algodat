from nodes import Nodes
from collections import deque

class DFS:
        
    def algorithm(start, end, nodeList):
        stack = deque([(start, [start.name])])
        currentNode = None
        
        for n in nodeList:
            n.visited = 0
        start.visited = 1

        while len(stack) != 0:
            currentNode, path = stack.pop()
            if currentNode == end:
                return path
            for nb in currentNode.neighbour:
                nb = nodeList[nb.name]
                if nb.visited != 1:
                    nb.visited = 1
                    new_path = path + [nb.name]
                    stack.append((nb, new_path))
        
        return None