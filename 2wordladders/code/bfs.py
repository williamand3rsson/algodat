from node import Node
class BFS:

    def algorithm(start, end, wordLib):
        counter = 0
        currentCount = 1
        allNeighbour = [start]
        currentNode = Node(start, wordLib)
        notDone = [start]
        oldNode = currentNode
        while len(notDone) != 0:
            currentNode.visited = 1
            for neighbour in currentNode.neighbourList:
                if neighbour.visited == 0:
                    neighbour.visited = 1
                    allNeighbour.append(neighbour)
                oldNode = currentNode
                currentNode = Node(allNeighbour[currentCount], wordLib)
                if oldNode == end:
                    print(counter)
                    return
                counter += 1
        else:
            print("Impossible")


        
            


