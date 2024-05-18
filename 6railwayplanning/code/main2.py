import sys
from ff import Ff
from nodes import Nodes
from bfs2 import BFS2
from edge import Edge
from ff2 import Ff2
import time

#behåll som vanligt funkar
counter = 0
students = 0
nbrEdges = 0
nodes = 0
quiries = 0
edges = {}
matcher = {}
reNodes = []
result1 = []
start2 = time.time()
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
        matcher[counter] = int(lines[0]), int(lines[1])
        matcher[-counter] = int(lines[1]), int(lines[0])
        edges[(int(lines[1]), int(lines[0]))] = Edge(int(lines[1]), int(lines[0]), int(lines[2]))
        edges[(int(lines[0]), int(lines[1]))] = Edge(int(lines[0]), int(lines[1]), int(lines[2]))
        nodeList[int(lines[1])].neighbour.append(nodeList[int(lines[0])])
        nodeList[int(lines[0])].neighbour.append(nodeList[int(lines[1])])
        counter += 1
    else:
        reNodes.append(int(line))

#kommer nu att få ut en path istället och det är den kortaste
counter = 0
preFlow = 0
resCount, resFlow = counter, 0
delList = []
flow = 0
totFlow = 0
#lösa flow och preflow, göra så att inte samma vägar välj hela tiden
while reNodes:
    print(len(edges), "längd")
    nodeToRemove = reNodes.pop(0)
    frontNode, backNode = matcher[nodeToRemove + 1]
    print(frontNode, backNode, "ta bort noder")
    while flow < students:
        flow = 0
        path = BFS2.algorithm(nodeList[0], nodeList[nodes - 1], nodeList)
        print(path, "vägen")
        flow += Ff2.ff(students, edges, path)
        print(flow, "flowet")
        #måste lösa sätt att ta sig ur här med
    if flow >= students:
            counter += 1
            resCount, resFlow = counter-1, flow
    print(resCount, resFlow, "resultatet")
    print("")
    #ta bort egdes 
    edges.pop((frontNode, backNode))
    edges.pop((backNode, frontNode))
    nodeList[frontNode].removeNb(nodeList[backNode])
    nodeList[backNode].removeNb(nodeList[frontNode])

    for e in edges.values():
        e.flow = 0
