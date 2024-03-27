from node import Node
class BFS:

    def algorithm(start, end, wordLib):
        counter = 0
        currentCount = 1
        allNeighbour = [start]
        currentNode = Node(start, wordLib)
        while counter <= 5000:
            currentNode.visited = 1
            counter += 1
            for neighbour in currentNode.neighbourList:
                allNeighbour.append(neighbour)
            currentNode = Node(allNeighbour[currentCount], wordLib)
            if end in allNeighbour:
                print(counter)
                return
        else:
            print("Impossible")


        
            


