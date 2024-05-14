import sys
from ff import Ff
from nodes import Nodes
from bfs import BFS
from edge import Edge

counter = 0
students = 0
nbrEdges = 0
nodes = 0
quiries = 0
edges = {}
matcher = {}
reNodes = []
for line in sys.stdin:
    lines = line.split()
    if counter == 0:
        nodes = int(lines[0])
        nbrEdges = int(lines[1])
        students = int(lines[2])
        quiries = int(lines[3])
        nodeList = [Nodes(i) for i in range(0 ,(nodes))]
        counter += 1
    elif counter < int(nbrEdges) + 1:
        matcher[counter] = [int(lines[0]), int(lines[1])]
        matcher[-counter] = [int(lines[1]), int(lines[0])]
        edges[(int(lines[1]), int(lines[0]))] = Edge(int(lines[1]), int(lines[0]), int(lines[2]))
        edges[(int(lines[0]), int(lines[1]))] = Edge(int(lines[0]), int(lines[1]), int(lines[2]))
        nodeList[int(lines[1])].neighbour.append(nodeList[int(lines[0])])
        nodeList[int(lines[0])].neighbour.append(nodeList[int(lines[1])])
        counter += 1
    else:
        reNodes.append(int(line[0]))

paths = BFS.bfs(nodeList[0], nodeList[nodes - 1], nodeList)
counter = 0
preFlow = 0

while reNodes:
    #print(paths)
    for path in paths:
        print(path)
        flow = Ff.ff(students, edges, path, preFlow)
        if flow >= students:
            counter += 1
            result = (counter, flow)
            break
    if flow < students:
        print(result)
        break
    print(reNodes)
    nodeToRemove = reNodes.pop(0)
    
    ## removes all paths with reNodes in them
    flow = preFlow = 0
    front1, front2 = matcher[nodeToRemove + 1]
    #back1, back2 = matcher[-nodeToRemove + 1]
    for i in range(len(paths)-1): 
        print(paths)
        if (paths[i] == front1 and paths[i+1] == front2) or (paths[i] == front2 and paths[i+1] == front1):
            paths.remove(path)
            print("hjsa")

    for e in edges.values():
        e.flow = 0

