from nodes import Nodes
from collections import deque

class BFS2:
        
    def algorithm(start, end, nodeList):
        queue = deque([(start, [start.name])])

        for node in nodeList:
            node.visited = 0

        start.visited = 1

        while queue:
            currentNode, path = queue.popleft()

            for nb in currentNode.neighbour:
                neighbour = nodeList[nb.name]

                if neighbour.visited == 0:
                    neighbour.visited = 1
                    new_path = path + [neighbour.name]
                    neighbour.pred = currentNode
                    if neighbour.name == end.name:
                        return new_path
                    queue.append((neighbour, new_path))
        return None

