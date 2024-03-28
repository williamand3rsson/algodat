from node import Node

class BFS:        

    def algorithm(start, end, nodeList, wordLib):
        qList = [(start, 1)]
        currentNode = None

        for n in nodeList:
            n.visited = 0
        start.visited = 1

        if(start.name == end.name):
            print("0")
            return

        while len(qList) != 0:
            currentNode, distance = qList.pop(0)
            for nb in currentNode.neighbourList:
                "DENNA SKA BORT"
                for node in nodeList:
                    if nb == node.name:
                        nb = node
                "DENNA SKA BORT"
                if nb.visited != 1:
                    nb.visited = 1
                    qList.append((nb, distance + 1))
                    nb.pred = currentNode
                    if(nb.name == end.name):
                        print(distance)
                        return
        print("Impossible")
