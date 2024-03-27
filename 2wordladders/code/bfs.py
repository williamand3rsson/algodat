from node import Node

class BFS:

    def algorithm(start, end, nodeList, wordLib):
        qList = [start]
        currentNode = None
        start.visited = 1
        counter = 0
        while qList is not None:
            currentNode = qList.pop()
            for nb in currentNode.neighbourList:
                nb = nodeList[nodeList.index(Node(nb, wordLib))]
                if nb.visited != 1:
                    nb.visited = 1
                    qList.append(nb)
                    nb.pred = currentNode
                    if(currentNode == end):
                        print(counter)
                        return
            counter += 1
        print("Impossible")

