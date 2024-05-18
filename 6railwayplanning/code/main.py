import sys
from ff import Ff
from nodes import Nodes
from bfs import BFS
from edge import Edge
import time
start1 = time.time()
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
end2 = time.time()

start = time.time()
paths = BFS.bfs(nodeList[0], nodeList[nodes - 1], nodeList)
#path = DFS.algorithm(nodeList[0], nodeList[nodes - 1], nodeList)
#print(path)
end = time.time()
print(end-start, "BFS")
counter = 0
preFlow = 0
resCount, resFlow = counter, 0
delList = []
while reNodes:
    print(paths)
    for path in paths:
        print(path)
        flow = Ff.ff(students, edges, path, preFlow)
        if flow >= students:
            print(flow)
            counter += 1
            resCount, resFlow = counter-1, flow
            break
        preFlow = flow
    if flow < students:
        print(resCount, resFlow)
        break
    nodeToRemove = reNodes.pop(0)
    flow = preFlow = 0
    front1, front2 = matcher[nodeToRemove + 1]
    #print(front1, front2)
    # print(paths)
    # #print(delList)
    # print(result1)
    # print(front1, front2)
    print("")
    for path in paths:
        for i in range(len(path)-1): 
            if ((path[i] == front1 and path[i+1] == front2) or (path[i] == front2 and path[i+1] == front1)) and path not in delList:
                delList.append(path)
        
    result1 = [x for x in paths if x not in delList] 
    # måste på något sätt få sä att result1 är nya path, samt nollställa result1 
    # kanske 
    paths = result1.copy()
    result1 = []

    for e in edges.values():
        e.flow = 0
end1 = time.time()
print(end1-start1)